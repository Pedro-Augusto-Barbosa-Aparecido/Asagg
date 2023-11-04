import unittest

from asagg_lib.asagg import Asagg


class TestAsaggGetter(unittest.TestCase):
    def setUp(self):
        self.expected_values = _expect = {
            "_edge": 10,
            "__border": 40,
            "__bod": 4,
        }

        @Asagg.getter
        class Square:
            def __init__(self):
                self._edge = _expect["_edge"]
                self.__border = _expect["__border"]
                self.__bod = _expect["__bod"]

        self.square = Square()

    def test_it_should_be_able_to_create_getter_to_private_and_protected_properties(
        self,
    ):
        list_of_the_members = self.square.__dir__()

        self.assertIn("edge", list_of_the_members)
        self.assertIn("border", list_of_the_members)
        self.assertIn("bod", list_of_the_members)

    def test_it_should_be_able_to_get_a_value_to_new_setter_property(self):
        """Test if getters is generate correctly"""
        self.assertEqual(self.expected_values["__bod"], self.square.bod)
        self.assertEqual(self.expected_values["__border"], self.square.border)
        self.assertEqual(self.expected_values["_edge"], self.square.edge)
