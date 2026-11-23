from core.abstract_dto import AbstractDto
from core.exception import OperationExeption
from core.validator import Validator
from models.user_model import UserModel


class UserDto(AbstractDto):

    __unique_code: str = ""
    __name: str = ""
    __lastname: str = ""
    __patronymic: str = ""
    __post_code: str = ""
    __subdivision_code: str = ""
    __email: str = ""
    __password: str = ""
    __min_length: int = 8

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

    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, value: str):
        Validator.validate(value, str, "lastname")
        self.__lastname = value.strip()

    @property
    def patronymic(self):
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, value: str):
        Validator.validate(value, str, "patronymic")
        self.__patronymic = value.strip()

    @property
    def post_code(self):
        return self.__post_code

    @post_code.setter
    def post_code(self, value: str):
        Validator.validate(value, str, "post_code")
        self.__post_code = value.strip()

    @property
    def subdivision_code(self):
        return self.__subdivision_code

    @subdivision_code.setter
    def subdivision_code(self, value: str):
        Validator.validate(value, str, "subdivision_code")
        self.__subdivision_code = value.strip()

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value: str):
        Validator.validate(value, str, "email")
        value = value.strip()
        Validator.check_email(value, "email")
        self.__email = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value: str):
        Validator.validate(value, str, "password")
        value = value.strip()
        Validator.validate(value, str, "password", min_len=self.__min_length)
        self.__password = value

    def from_domain_model(self, source: UserModel):
        Validator.validate(source, UserModel, "from_domain_model")

        dto = UserDto()
        dto.unique_code = source.unique_code
        dto.name = source.name
        dto.lastname = source.lastname
        dto.patronymic = source.patronymic

        if source.post is not None:
            dto.post_code = source.post.unique_code

        if source.subdivision is not None:
            dto.subdivision_code = source.subdivision.unique_code

        dto.email = source.email
        dto.password = source.password

        return dto

    def from_dict(self, source: dict):
        Validator.require_keys(
            source,
            (
                "unique_code", "name", "lastname", "patronymic",
                "post_code", "subdivision_code", "email", "password",
            ),
            "source",
        )

        self.unique_code = source["unique_code"]
        self.name = source["name"]
        self.lastname = source["lastname"]
        self.patronymic = source["patronymic"]
        self.post_code = source["post_code"]
        self.subdivision_code = source["subdivision_code"]
        self.email = source["email"]
        self.password = source["password"]

        return self

    def mapping(self, cache:dict):
        super().mapping(cache)

        domain = UserModel()
        domain.unique_code = self.unique_code
        domain.name = self.name
        domain.lastname = self.lastname
        domain.patronymic = self.patronymic

        if self.post_code not in cache.keys():
            raise OperationExeption("mapping", f"Невозможно получить объект с кодом {self.post_code} из хранилища!")

        if self.subdivision_code not in cache.keys():
            raise OperationExeption("mapping", f"Невозможно получить объект с кодом {self.subdivision_code} из хранилища!")

        domain.post = cache[self.post_code]
        domain.subdivision = cache[self.subdivision_code]
        domain.email = self.email
        domain.password = self.password
        cache[ domain.unique_code ] = domain

        return domain
