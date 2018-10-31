from .xml_base import XMLModelBase
from snomedct.models import SnomedConcept, ReadCode


class SocialConsultationElement(XMLModelBase):
    XPATH = ".//ConsultationElement[Header/Term='Social']"

    def date(self) -> str:
        return self.get_element_text('Event/AssignedDate')

    def description(self) -> str:
        return (
            self.get_element_text('Event/DisplayTerm')
            or self.get_element_text('Event/Code/Term')
        )

    def is_smoking(self) -> bool:
        return self.__code_descendent_of(self.__smoking_concept())

    def is_alcohol(self) -> bool:
        return self.__code_descendent_of(self.__alcohol_concept())

    # private
    def __smoking_concept(self) -> SnomedConcept:
        return SnomedConcept.objects.get(external_id='365981007')

    def __alcohol_concept(self) -> SnomedConcept:
        return SnomedConcept.objects.get(external_id='228273003')

    def __code_descendent_of(self, snomed_model: SnomedConcept) -> bool:
        readcodes = self.readcodes()
        if readcodes:
            descendant_readcodes = map(
                lambda rc: rc.ext_read_code,
                snomed_model.descendant_readcodes()
            )
            return not set(readcodes).isdisjoint(descendant_readcodes)
        else:
            descendant_concepts = map(
                lambda sc: sc.external_id,
                snomed_model.descendants()
            )
            return not set(
                map(int, self.snomed_concepts())
            ).isdisjoint(descendant_concepts)
