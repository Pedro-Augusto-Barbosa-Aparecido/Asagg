from abc import ABCMeta, abstractmethod

from jinja2 import Environment, FileSystemLoader


class TemplateGenerator(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    def generate_type_file(self, template_name: str, data: dict):
        ...
