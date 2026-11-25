from abc import ABC
import uuid


class AbstractModel(ABC):

    __unique_code: str
    __type: str = ""

    def __init__(self) -> None:
        super().__init__()
        self.__unique_code = uuid.uuid4().hex

    @property
    def unique_code(self) -> str:
        return self.__unique_code

    @unique_code.setter
    def unique_code(self, value: str) -> None:
        self.__unique_code = value.strip()

    @property
    def item_type(self) -> str:
        return self.__type

    @item_type.setter
    def item_type(self, value: str) -> None:
        self.__type = value

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, AbstractModel):
            return False
        return self.unique_code == value.unique_code

    def __hash__(self) -> int:
        return hash(self.unique_code)