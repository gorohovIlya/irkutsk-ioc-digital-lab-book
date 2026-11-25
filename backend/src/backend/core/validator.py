from .exception import (
    ArgumentsException,
    MaxLengthException,
    MinLengthException,
    LengthException,
    ValidationExecption,
    FileException,
    EmptyFileException,
    IncorrectEmail,
)

import os
import re


class Validator:

    @staticmethod
    def validate(value, type_, field="field"):
        if value is None:
            raise ArgumentsException(field, "Пустой аргумент")

        if isinstance(value, str) and value.strip() == "":
            raise ArgumentsException(field, "Пустой аргумент")

        if value == "":
            raise ArgumentsException(field, "Пустой аргумент")

        if not isinstance(value, type_):
            raise ArgumentsException(field, "Некорректно переданный аргумент")

    @staticmethod
    def incorrect_length(value, field="field", leng=None, document="document"):
        if leng is not None and len(str(value).strip()) != leng:
            raise LengthException(field, leng, document)

    @staticmethod
    def incorrect_max_length(value, field="field", max_len=None):
        if max_len is not None and len(str(value).strip()) > max_len:
            raise MaxLengthException(field, max_len)

    @staticmethod
    def incorrect_min_length(value, field="field", min_len = None):
        if min_len is not None and len(str(value).strip()) < min_len:
            raise MinLengthException(field, min_len)

    @staticmethod
    def digit_validate(value, field="field"):
        Validator.validate(value, str, field)
        if not value.isdigit():
            raise ValidationExecption(field, "Аргумент должен содержать только числовые значения")

    @staticmethod
    def no_lower_that_zero_validate(value, field="field"):
        if value <= 0:
            raise ArgumentsException(field, "Аргумент должен быть больше нуля")

    @staticmethod
    def require_keys(data, keys, field="data"):
        if not isinstance(data, dict):
            raise ArgumentsException(field, "Должен быть словарём")

        for key in keys:
            if key not in data:
                raise ArgumentsException(
                    f"{field}.{key}",
                    f"Отсутствует обязательный ключ '{key}' в {field}"
                )

    @staticmethod
    def require_dict(data, field="data"):
        if not isinstance(data, dict):
            raise ArgumentsException(field, "Должен быть объектом (словарём)")

    @staticmethod
    def file_not_exist(data, field="data"):
        if not os.path.exists(data):
            raise FileException(field, data)

    @staticmethod
    def empty_file(data, field="data"):
        Validator.file_not_exist(data, field)
        if os.path.getsize(data) == 0:
            raise EmptyFileException(field, data)

    @staticmethod
    def check_email(value, field="check_email"):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, value) is None:
            raise IncorrectEmail(field, "Email написан неправильно!")
