from core.abstract_dto import AbstractDto
from models.subdivision_model import SubdivisionModel
from core.validator import Validator


class SubdivisionDto(AbstractDto):

    __unique_code: str = ""
    __name: str = ""

    @property
    def unique_code(self) -> str:
        return self.__unique_code

    @unique_code.setter
    def unique_code(self, value: str) -> None:
        Validator.validate(value, str, "unique_code")
        self.__unique_code = value.strip()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        Validator.validate(value, str, "name")
        self.__name = value.strip()

    def from_domain_model(self, source: SubdivisionModel):
        Validator.validate(source, SubdivisionModel, "from_domain_model")

        dto = SubdivisionDto()
        dto.unique_code = source.unique_code
        dto.name = source.name

        return dto

    def from_dict(self, source: dict):
        Validator.require_keys(source, ("unique_code", "name"), "source")

        self.unique_code = source["unique_code"]
        self.name = source["name"]

        return self

    def mapping(self, cache:dict):
        super().mapping(cache)

        domain = SubdivisionModel()
        domain.unique_code = self.unique_code
        domain.name = self.name

        cache[ domain.unique_code ] = domain

        return domain
