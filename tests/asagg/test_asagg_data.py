import unittest

from asagg_lib.asagg import Asagg


class TestAsaggData(unittest.TestCase):
    def setUp(self):
        self.expected_values = _expect = {
            "_edge": 10,
            "_edge_after": 20,
            "_foo": 40,
        }

        @Asagg.data
        class Square:
            def __init__(self):
                self._edge = _expect["_edge"]
                self._foo = _expect["_foo"]

        self.square = Square()

    def test_it_should_be_able_to_create_getter_and_setter_to_private_and_protected_properties(
        self,
    ):
        list_of_the_members = self.square.__dir__()

        self.assertIn("edge", list_of_the_members)
        self.assertIn("foo", list_of_the_members)

    def test_it_should_be_able_to_set_and_get_a_value_to_new_setter_property(
        self,
    ):
        self.square.edge = self.expected_values["_edge_after"]
        self.assertEqual(self.expected_values["_edge_after"], self.square.edge)
        self.assertEqual(self.expected_values["_foo"], self.square.foo)
