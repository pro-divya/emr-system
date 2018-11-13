from django.db import models
from django import forms
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.core.mail import send_mail
from django.core.exceptions import ValidationError
from common.models import TimeStampedModel
from accounts.models import ClientUser, GeneralPracticeUser, Patient, MedidataUser, User
from accounts import models as account_models
from snomedct.models import SnomedConcept
from .model_choices import *
from common.functions import get_env_variable
from django.conf import settings
PIPELINE_INSTRUCTION_LINK = settings.PIPELINE_INSTRUCTION_LINK
TITLE_CHOICE = account_models.TITLE_CHOICE

from typing import List, Set


class Instruction(TimeStampedModel, models.Model):
    client_user = models.ForeignKey(ClientUser, on_delete=models.CASCADE, verbose_name='Client', null=True)
    gp_user = models.ForeignKey(GeneralPracticeUser, on_delete=models.CASCADE, verbose_name='GP Allocated', null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='Patient')
    completed_signed_off_timestamp = models.DateTimeField(null=True, blank=True)
    rejected_timestamp = models.DateTimeField(null=True, blank=True)
    rejected_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    rejected_note = models.TextField(blank=True)
    rejected_reason = models.IntegerField(choices=INSTRUCTION_REJECT_TYPE, null=True, blank=True)
    type = models.CharField(max_length=4, choices=INSTRUCTION_TYPE_CHOICES)
    final_report_date = models.TextField(blank=True)
    initial_monetary_value = models.FloatField(null=True, blank=True, verbose_name='Value £')
    status = models.IntegerField(choices=INSTRUCTION_STATUS_CHOICES, default=INSTRUCTION_STATUS_NEW)
    consent_form = models.FileField(upload_to='consent_forms', null=True, blank=True)
    gp_title_from_client = models.CharField(max_length=5, choices=TITLE_CHOICE, blank=True)
    gp_initial_from_client = models.CharField(max_length=20, blank=True)
    gp_last_name_from_client = models.CharField(max_length=255, blank=True)

    gp_practice_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    gp_practice_id = models.CharField(max_length=255)
    gp_practice = GenericForeignKey('gp_practice_type', 'gp_practice_id')
    sars_consent = models.FileField(upload_to='consent_forms', null=True, blank=True)
    mdx_consent = models.FileField(upload_to='consent_forms', null=True, blank=True)
    saved = models.BooleanField(default=False)

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

    def reject(self, request, context):
        self.rejected_timestamp = timezone.now()
        self.rejected_by = request.user
        self.rejected_reason = context.get('rejected_reason', None)
        self.rejected_note = context.get('rejected_note', '')
        self.status = INSTRUCTION_STATUS_REJECT
        if self.client_user:
            self.send_reject_email([self.client_user.user.email])
        if self.gp_user and self.gp_user.role == GeneralPracticeUser.OTHER_PRACTICE:
            emails = [medi.user.email for medi in MedidataUser.objects.all()]
            self.send_reject_email(emails)
        self.save()

    def send_reject_email(self, to_email):
        send_mail(
            'Rejected Instruction',
            'You have a rejected instruction. Click here {link}?status=4&type=allType to see it.'.format(link=PIPELINE_INSTRUCTION_LINK),
            'MediData',
            to_email,
            fail_silently=True,
            auth_user=settings.EMAIL_HOST_USER,
            auth_password=settings.EMAIL_HOST_PASSWORD,
        )

    def snomed_concepts_ids(self) -> Set[int]:
        snomed_concepts_ids = set()
        for sct in self.selected_snomed_concepts():
            snomed_concepts_ids.update(
                map(lambda sc: sc.external_id, sct.descendants())
            )
        return snomed_concepts_ids

    def readcodes(self) -> Set[str]:
        readcodes = set()
        for sct in self.selected_snomed_concepts():
            readcodes.update(
                map(lambda rc: rc.ext_read_code, sct.descendant_readcodes())
            )
        return readcodes

    def selected_snomed_concepts(self):
        return SnomedConcept.objects.filter(
            instructionconditionsofinterest__instruction=self.id
        )


class InstructionAdditionQuestion(models.Model):
    instruction = models.ForeignKey(Instruction, on_delete=models.CASCADE, related_name='addition_questions')
    question = models.CharField(max_length=255, blank=True)
    response_mandatory = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Instruction Addition Question"

    def __str__(self):
        return self.question


class InstructionAdditionAnswer(models.Model):
    question = models.OneToOneField(InstructionAdditionQuestion, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = "Instruction Addition Answer"

    def __str__(self):
        return self.answer


class InstructionConditionsOfInterest(models.Model):
    instruction = models.ForeignKey(Instruction, on_delete=models.CASCADE)
    snomedct = models.ForeignKey(SnomedConcept, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Instruction Conditions Of Interest"

    def __str__(self):
        return "{} ({})".format(self.snomedct.fsn_description, self.snomedct.external_id)


class Setting(models.Model):
    consent_form = models.FileField(upload_to='consent_forms', null=True, blank=True)
    policy_form = models.FileField(upload_to='policy_forms', null=True, blank=True)
    site = models.URLField(max_length=255, blank=True)

    def save(self, *args, **kwargs):
        self.__class__.objects.exclude(id=self.id).delete()
        super(Setting, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        try:
            return cls.objects.get()
        except cls.DoesNotExist:
            return cls()
