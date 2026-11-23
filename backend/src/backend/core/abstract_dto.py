from abc import ABC, abstractmethod
from core.abstract_model import AbstractModel
from core.validator import Validator

class AbstractDto(ABC):

    @abstractmethod
    def from_domain_model(self, source: AbstractModel):
        pass

    @abstractmethod
    def mapping(self, cache:dict):
        Validator.validate(cache, dict)     
        pass

    @abstractmethod 
    def from_dict(self, source:dict):
        pass

    def try_get_value(self, key:str, source:dict) -> object:
        Validator.validate(key, str)
        Validator.validate(source, dict)

        if key in source.keys():
            return source[ key ]
        else:
            return None
