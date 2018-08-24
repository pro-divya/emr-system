from . import xml_utils
import datetime


class XMLBase(object):
    def __init__(self, xml_data):
        self.parsed_xml = xml_utils.xml_parse(xml_data)


class XMLModelBase(XMLBase):
    def parsed_date(self):
        date = self.date()
        if date is not None:
            return datetime.datetime.strptime(date, "%d/%m/%Y")
        else:
            return None

    def readcodes(self):
        codes = self.parsed_xml.findall(".//Code[Scheme='READ2']/Value")
        return [code.text for code in codes]

    def snomed_concepts(self):
        snomeds = self.parsed_xml.findall(".//Code[Scheme='SNOMED']/Value")
        return [snomed.text for snomed in snomeds]