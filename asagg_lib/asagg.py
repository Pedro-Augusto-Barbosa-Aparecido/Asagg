from abc import ABC, abstractmethod
from typing import Any, Callable

from asagg_lib.typing.generics import ClassType
from asagg_lib.utils.extractor import Extractor


class Assag(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @staticmethod
    def data(_class):
        return _class

    @staticmethod
    def getter(_class: ClassType):
        attrs = Extractor.extract_attributes(_class)
        classname = Extractor.extract_name_of_class(_class)

        new_attributes = []
        for attr in attrs:
            value_of_property: Callable[
                [], type(getattr(_class, attr))
            ] = Assag._default_getter(attr)

            attr = attr.replace("_", "")
            if classname in attr:
                attr = attr.replace(classname, "")

            setattr(_class, attr, value_of_property)
            new_attributes.append(attr)

            del value_of_property

        for new_attr in new_attributes:
            _class.__annotations__[new_attr] = type(getattr(_class, new_attr))

        return _class

    @staticmethod
    def setter(_class):
        return _class

    @staticmethod
    def _default_getter(attr):
        return property(lambda self: getattr(self, attr))
