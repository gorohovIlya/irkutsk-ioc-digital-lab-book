from typing import Optional
from core.entity_model import EntityModel
from core.validator import Validator
from models.post_model import PostModel
from models.subdivision_model import SubdivisionModel


class UserModel(EntityModel):

    __post: Optional[PostModel] = None
    __subdivision: Optional[SubdivisionModel] = None
    __lastname: str = ""
    __patronymic: str = ""
    __email: str = ""
    __password: str = ""
    __min_length: int = 8

    def __init__(self,name: Optional[str] = None,lastname: Optional[str] = None,patronymic: Optional[str] = None,post: Optional[PostModel] = None,subdivision: Optional[SubdivisionModel] = None,email: Optional[str] = None,password: Optional[str] = None) -> None:
        super().__init__()
        if name is not None:
            self.name = name
        if lastname is not None:
            self.lastname = lastname
        if patronymic is not None:
            self.patronymic = patronymic
        if post is not None:
            self.post = post
        if subdivision is not None:
            self.subdivision = subdivision
        if email is not None:
            self.email = email
        if password is not None:
            self.password = password

    @property
    def post(self) -> Optional[PostModel]:
        return self.__post

    @post.setter
    def post(self, value: Optional[PostModel]) -> None:
        if value is not None:
            Validator.validate(value, PostModel, "post")
        self.__post = value

    @property
    def subdivision(self) -> Optional[SubdivisionModel]:
        return self.__subdivision

    @subdivision.setter
    def subdivision(self, value: Optional[SubdivisionModel]) -> None:
        if value is not None:
            Validator.validate(value, SubdivisionModel, "subdivision")
        self.__subdivision = value

    @property
    def lastname(self) -> str:
        return self.__lastname

    @lastname.setter
    def lastname(self, value: str) -> None:
        Validator.validate(value, str, "lastname")
        self.__lastname = value.strip()

    @property
    def patronymic(self) -> str:
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, value: str) -> None:
        Validator.validate(value, str, "patronymic")
        self.__patronymic = value.strip()

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, value: str) -> None:
        Validator.validate(value, str, "email")
        value = value.strip()
        Validator.check_email(value, "email")
        self.__email = value

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, value: str) -> None:
        Validator.validate(value, str, "password")
        value = value.strip()
        Validator.validate(value, str, "password", min_len=self.__min_length)
        self.__password = value

    @classmethod
    def create(cls,name: str,lastname: str,patronymic: str,post: Optional[PostModel],subdivision: Optional[SubdivisionModel],email: str,password: str):
        return cls(name=name,lastname=lastname,patronymic=patronymic,post=post,subdivision=subdivision,email=email,password=password)
