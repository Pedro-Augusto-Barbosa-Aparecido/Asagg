from typing import Protocol, runtime_checkable


@runtime_checkable
class ClassType(Protocol):
    def __init__(self):
        pass
