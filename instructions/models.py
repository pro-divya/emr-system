from django.db import models
from django import forms
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.core.mail import send_mail
from django.core.exceptions import ValidationError
from common.models import TimeStampedModel
from accounts.models import ClientUser, GeneralPracticeUser, Patient, MedidataUser
from snomedct.models import SnomedConcept
from .model_choices import *
from common.functions import get_env_variable
from django.conf import settings
PIPELINE_INSTRUCTION_LINK = settings.PIPELINE_INSTRUCTION_LINK

from typing import List, Tuple


class Instruction(TimeStampedModel, models.Model):
    client_user = models.ForeignKey(ClientUser, on_delete=models.CASCADE, verbose_name='Client', null=True)
    gp_user = models.ForeignKey(GeneralPracticeUser, on_delete=models.CASCADE, verbose_name='GP Allocated', null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='Patient')
    completed_signed_off_timestamp = models.DateTimeField(null=True, blank=True)
    rejected_timestamp = models.DateTimeField(null=True, blank=True)
    rejected_note = models.TextField(blank=True)
    rejected_reason = models.IntegerField(choices=INSTRUCTION_REJECT_TYPE, null=True, blank=True)
    type = models.CharField(max_length=4, choices=INSTRUCTION_TYPE_CHOICES)
    final_report_date = models.TextField(blank=True)
    initial_monetary_value = models.FloatField(null=True, blank=True, verbose_name='Value £')
    status = models.IntegerField(choices=INSTRUCTION_STATUS_CHOICES, default=INSTRUCTION_STATUS_NEW)
    consent_form = models.FileField(upload_to='consent_forms', null=True, blank=True)

    gp_practice_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    gp_practice_id = models.CharField(max_length=255)
    gp_practice = GenericForeignKey('gp_practice_type', 'gp_practice_id')

    class Meta:
        verbose_name = "Instruction"
        ordering = ('-created',)

    def __str__(self):
        return 'Instruction #{pk}'.format(pk=self.pk)

    def in_progress(self, context):
        self.status = INSTRUCTION_STATUS_PROGRESS
        if not self.gp_user:
            self.gp_user = context.get('gp_user', None)
        self.save()

    def reject(self, context):
        self.rejected_timestamp = timezone.now()
        self.rejected_reason = context.get('rejected_reason', None)
        self.rejected_note = context.get('rejected_note', None)
        self.status = INSTRUCTION_STATUS_REJECT
        self.send_reject_email([self.client_user.user.email])
        if self.gp_user and self.gp_user.role == GeneralPracticeUser.SARS_RESPONDER:
            emails = [medi.user.email for medi in MedidataUser.objects.all()]
            self.send_reject_email(emails)
        self.save()

    def send_reject_email(self, to_email):
        send_mail(
            'Rejected Instruction',
            'You have a rejected instruction. Click here {link}?status=4&type=allType to see it.'.format(link=PIPELINE_INSTRUCTION_LINK),
            'MediData',
            to_email,
            fail_silently=False,
            auth_user=get_env_variable('SENDGRID_USER'),
            auth_password=get_env_variable('SENDGRID_PASS'),
        )

    # JT - this is not a nice function. Should be rewritten with one function
    # for snomed_concepts, one function for readcodes.
    # todo: delete this method.
    def snomed_concepts_readcodes(self) -> Tuple[List[int], List[str]]:
        snomed_concepts_list = []
        readcodes_list = []
        for snomed_concept in self.selected_snomed_concepts():
            snomed_concepts_list.append(snomed_concept.external_id)
            for snomed_descendant in snomed_concept.snomed_descendants():
                snomed_concepts_list.append(snomed_descendant.external_id)

            for readcode in snomed_concept.combined_readcodes():
                readcodes_list.append(readcode.ext_read_code)

        return snomed_concepts_list, readcodes_list

    def snomed_concepts_ids(self) -> List[int]:
        snomed_concepts_ids = []
        for sct in self.selected_snomed_concepts():
            snomed_concepts_ids.append(sct.external_id)
            for sd in sct.snomed_descendants():
                snomed_concepts_ids.append(sd.external_id)
        return snomed_concepts_ids

    def readcodes(self) -> List[str]:
        readcodes = []
        for snomed_concept in self.selected_snomed_concepts():
            readcodes += [
                rc.ext_read_code for rc in snomed_concept.combined_readcodes()
            ]
        return readcodes

    def selected_snomed_concepts(self):
        return SnomedConcept.objects.filter(instructionconditionsofinterest__instruction=self.id)


class InstructionAdditionQuestion(models.Model):
    instruction = models.ForeignKey(Instruction, on_delete=models.CASCADE)
    question = models.CharField(max_length=255, blank=True)
    response_mandatory = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Instruction Addition Question"

    def __str__(self):
        return self.question


class InstructionConditionsOfInterest(models.Model):
    instruction = models.ForeignKey(Instruction, on_delete=models.CASCADE)
    snomedct = models.ForeignKey(SnomedConcept, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Instruction Conditions Of Interest"

    def __str__(self):
        return "{} ({})".format(self.snomedct.fsn_description, self.snomedct.external_id)
