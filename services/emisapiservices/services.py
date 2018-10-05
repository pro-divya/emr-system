from django.conf import settings
import urllib
import requests
from ..models import EmisAPIConfig


class EmisAPIServiceBase(object):
    def __init__(self):
        self.emis_api_config = EmisAPIConfig.objects.first()
        if self.emis_api_config is None:
            raise ValueError('Unable to get EMIS API Configuration')

    def uri(self):
        raise NotImplementedError(
            "Inheriting classes must implement this method."
        )

    def call(self):
        request_uri = self.uri()
        r = requests.get(
            request_uri,
            auth=(
                self.emis_api_config.emis_username,
                self.emis_api_config.emis_password
            )
        )
        r.raise_for_status()
        return r.text


class GetAttachment(EmisAPIServiceBase):
    def __init__(self, patient_number, attachment_identifier):
        super().__init__()
        self.patient_number = patient_number
        self.attachment_identifier = attachment_identifier

    def uri(self):
        uri = "{host}/api/organisations/{organisation_id}/patients/{patient_number}/attachments/{attachment_identifier}".format(
            host=settings.EMIS_API_HOST,
            organisation_id=self.emis_api_config.emis_organisation_id,
            patient_number=self.patient_number,
            attachment_identifier=urllib.parse.quote(self.attachment_identifier, safe=''))
        return uri


class GetPatientList(EmisAPIServiceBase):
    def __init__(self, patient):
        super().__init__()
        self.patient = patient

    def search_term(self):
        terms = [self.patient.first_name, self.patient.last_name, self.patient.dob.strftime("%d/%m/%Y")]
        terms = list(filter(None, terms))
        terms = " ".join(terms)
        return urllib.parse.quote(terms, safe='')

    def uri(self):
        uri = "{host}/api/organisations/{organisation_id}/patients?q={search_term}".format(
            host=settings.EMIS_API_HOST,
            organisation_id=self.emis_api_config.emis_organisation_id,
            search_term=self.search_term())
        return uri


class GetMedicalRecord(EmisAPIServiceBase):
    def __init__(self, patient_number):
        super().__init__()
        self.patient_number = patient_number

    def uri(self):
        uri = "{host}/api/organisations/{organisation_id}/patients/{patient_number}/medical_record".format(
            host=settings.EMIS_API_HOST,
            organisation_id=self.emis_api_config.emis_organisation_id,
            patient_number=self.patient_number)
        return uri
