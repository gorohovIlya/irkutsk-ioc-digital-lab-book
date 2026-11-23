from .abstract_model import AbstractModel
from .validator import Validator


class EntityModel(AbstractModel):

    __name: str = ""
    __max_length: int = 150

    def __init__(self, name: str = "") -> None:
        super().__init__()
        if name:
            self.name = name

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        Validator.validate(value, str, "name")
        self.__name = value.strip()

    @property
    def max_length(self) -> int:
        return self.__max_length

    @max_length.setter
    def max_length(self, value: int) -> None:
        Validator.validate(value, int, "max_length")
        Validator.no_lower_that_zero_validate(value, "max_length")
        self.__max_length = value

    @property
    def max_lenght(self) -> int:
        return self.max_length

    @max_lenght.setter
    def max_lenght(self, value: int) -> None:
        self.max_length = value
