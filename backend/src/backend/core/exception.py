class AppBaseException(Exception):
    __message: str = ""
    __field: str = ""
    __stack_trace: str = ""

    def __init__(self, field: str, message: str, stack_trace: str = "") -> None:
        self.__field = (field or "").strip()
        self.__message = (message or "").strip()
        self.__stack_trace = (stack_trace or "").strip()
        super().__init__(self.__message)

    @property
    def field(self) -> str:
        return self.__field

    @property
    def message(self) -> str:
        return self.__message

    @property
    def stack_trace(self) -> str:
        """Возвращает трассировку стека (при наличии)."""
        return self.__stack_trace

    def __str__(self) -> str:
        return (
            f"Ошибка: Некорректный аргумент!\n"
            f"Поле: {self.__field}\n"
            f"{self.__message}\n"
            f"{self.__stack_trace}"
        )


class ArgumentsException(AppBaseException):

    def __init__(self, field: str, message: str, stack_trace: str = "") -> None:
        super().__init__(field, message, stack_trace)


class MaxLengthException(AppBaseException):
    def __init__(self, field: str, max_length: int, stack_trace: str = "") -> None:
        message = f"Превышена максимальная длина поля ({max_length} символов)"
        super().__init__(field, message, stack_trace)


class MinLengthException(AppBaseException):
    def __init__(self, field: str, min_length: int, stack_trace: str = "") -> None:
        message = f"Минимальная длина поля должна составлять ({min_length} символов)"
        super().__init__(field, message, stack_trace)


class LengthException(AppBaseException):
    def __init__(self, field: str, length: int, document: str,
                 stack_trace: str = "") -> None:
        message = f"Некорректная длина {document}! Она должна быть {length} символов"
        super().__init__(field, message, stack_trace)


class ValidationException(AppBaseException):
    def __init__(self, field: str, message: str, stack_trace: str = "") -> None:
        super().__init__(field, message, stack_trace)


class FileException(AppBaseException):
    def __init__(self, field: str, document: str, stack_trace: str = ""):
        message = f"Файл {document} не найден!"
        super().__init__(field, message, stack_trace)


class EmptyFileException(AppBaseException):
    def __init__(self, field: str, document: str, stack_trace: str = ""):
        message = f"Файл {document} пустой"
        super().__init__(field, message, stack_trace)


class IncorrectEmail(AppBaseException):
    def __init__(self, field: str, message: str, stack_trace: str = ""):
        super().__init__(field, message, stack_trace)


class OperationException(AppBaseException):
    def __init__(self, field: str, message: str, stack_trace: str = ""):
        super().__init__(field, message, stack_trace)
