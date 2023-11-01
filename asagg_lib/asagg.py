from abc import ABC, abstractmethod
from typing import Any, Callable

from asagg_lib.typing.generics import ClassType
from asagg_lib.utils.extractor import Extractor


class Assag(ABC):
    """
    An abstract base class for generating getters and setters for private and protected attributes.
    This class provides methods to generate getters for private and protected attributes of a given class.

    Methods:
        __init__
            This is an abstract method that must be implemented by subclasses.
        data(_class):
            A static method that returns the input class '_class' with getters and setters generateds.

        getter(_class):
            A static method that generates getters for private and protected attributes for the input class '_class'.

        setter(_class):
            A static method that generates setters for private and protected attributes for the input class '_class'.

        _default_getter(attr):
            A static method that returns a default getter for the specified attribute 'attr'.
    """

    @abstractmethod
    def __init__(self):
        """Absatract method"""
        pass

    @staticmethod
    def data(_class):
        return _class

    @staticmethod
    def getter(_class: ClassType) -> ClassType:
        """
        Generate Getters for all **private** and **protected** attributes for '_class', this method modify the class structure
        to generate a getter, adding new functions and properties

        Parameters:
            _class: this parameter is a class that will be generated the getters

        Returns:
            The return is the same class, but the class has getters for private and protected attributes

        """
        attrs = Extractor.extract_attributes(_class)
        classname = Extractor.extract_name_of_class(_class)

        new_attributes = []
        for attr in attrs:
            value_of_property: property = Assag._default_getter(attr)

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
