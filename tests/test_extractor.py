import unittest

import pytest

from asagg_lib.utils.extractor import Extractor
from asagg_lib.utils.list_operations import difference_between_lists


class Square:
    def __init__(self, edge_size: int):
        self._edge_size = edge_size
        self.__edge = edge_size
        self.edge = edge_size


ATTRIBUTES_SQUARE = ["_edge_size", "__edge", "edge"]


class TestExtractor(unittest.TestCase):
    def setUp(self):
        super(TestExtractor, self).setUp()
        self.extractor = Extractor

    def test_extractor_attributes(self):
        attributes = self.extractor.extract_attributes(Square)

        verification_list = []
        for attr in attributes:
            verification_list.append(
                any([expect_attr in attr for expect_attr in ATTRIBUTES_SQUARE])
            )

        is_collect_all_attrs = all(verification_list)

        self.assertTrue(
            is_collect_all_attrs,
            f"""
            Attributes collect: {attributes}
            Attributes expected: {ATTRIBUTES_SQUARE}
            Missign attributes: [{difference_between_lists(attributes, ATTRIBUTES_SQUARE)}]
        """.strip(),
        )

    def test_extractor_name(self):
        name_extracted = self.extractor.extract_name_of_class(Square)

        self.assertEqual(
            "Square",
            name_extracted,
            f"""
            Name expected: 'Square'
            Name collected: {name_extracted}
        """.strip(),
        )
