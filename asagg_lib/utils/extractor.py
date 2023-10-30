from abc import ABC, abstractmethod
from inspect import getmembers
from typing import List

from asagg_lib.typing.generics import ClassType


class Extractor(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @staticmethod
    def extract_attributes(_class: ClassType) -> List[str]:
        attributes = []
        for member in getmembers(_class):
            if "__init__" in member:
                attributes = member[1].__code__.co_names
                break

        return attributes

    @staticmethod
    def extract_name_of_class(_class: ClassType) -> str:
        return _class.__name__
