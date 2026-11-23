from .exception import (
    ArgumentsExeption,
    MaxLengthExeption,
    MinLengthExeption,
    LengthExeption,
    ValidationExeption,
    FileExeption,
    EmptyFileExeption,
    IncorrectEmail,
)

import os
import re


class Validator:

    @staticmethod
    def validate(value, type_, field="field", leng=None, max_len=None, min_len=None, document=None):
        if value is None:
            raise ArgumentsExeption(field, "Пустой аргумент")

        if isinstance(value, str) and value.strip() == "":
            raise ArgumentsExeption(field, "Пустой аргумент")

        if value == "":
            raise ArgumentsExeption(field, "Пустой аргумент")

        if not isinstance(value, type_):
            raise ArgumentsExeption(field, "Некорректно переданный аргумент")

        if leng is not None and len(str(value).strip()) != leng:
            raise LengthExeption(field, leng, document)

        if max_len is not None and len(str(value).strip()) > max_len:
            raise MaxLengthExeption(field, max_len)

        if min_len is not None and len(str(value).strip()) < min_len:
            raise MinLengthExeption(field, min_len)

    @staticmethod
    def digit_validate(value, field="field"):
        Validator.validate(value, str, field)
        if not value.isdigit():
            raise ValidationExeption(field, "Аргумент должен содержать только числовые значения")

    @staticmethod
    def no_lower_that_zero_validate(value, field="field"):
        if value <= 0:
            raise ArgumentsExeption(field, "Аргумент должен быть больше нуля")

    @staticmethod
    def require_keys(data, keys, field="data"):
        if not isinstance(data, dict):
            raise ArgumentsExeption(field, "Должен быть словарём")

        for key in keys:
            if key not in data:
                raise ArgumentsExeption(
                    f"{field}.{key}",
                    f"Отсутствует обязательный ключ '{key}' в {field}"
                )

    @staticmethod
    def require_dict(data, field="data"):
        if not isinstance(data, dict):
            raise ArgumentsExeption(field, "Должен быть объектом (словарём)")

    @staticmethod
    def file_not_exist(data, field="data"):
        if not os.path.exists(data):
            raise FileExeption(field, data)

    @staticmethod
    def empty_file(data, field="data"):
        Validator.file_not_exist(data, field)
        if os.path.getsize(data) == 0:
            raise EmptyFileExeption(field, data)

    @staticmethod
    def check_email(value, field="check_email"):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, value) is None:
            raise IncorrectEmail(field, "Email написан неправильно!")
