from typing import Protocol, runtime_checkable


@runtime_checkable
class ClassType(Protocol):
    """
    Interface to represent a type 'class'

    Methods:
        __init__():
            initialization method
    """

    def __init__(self):
        pass
