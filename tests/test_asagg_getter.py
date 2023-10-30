import unittest

from asagg_lib.asagg import Assag


class TestAsaggGetter(unittest.TestCase):
    def setUp(self):
        self.expected_values = _expect = {
            "_edge": 10,
            "__border": 40,
            "__bod": 4,
        }

        @Assag.getter
        class Square:
            def __init__(self):
                self._edge = _expect["_edge"]
                self.__border = _expect["__border"]
                self.__bod = _expect["__bod"]

        self.square = Square()

    def test_asagg_getter_generator(self):
        """Test if getters is generate correctly"""
        self.assertEqual(self.expected_values["__bod"], self.square.bod)
        self.assertEqual(self.expected_values["__border"], self.square.border)
        self.assertEqual(self.expected_values["_edge"], self.square.edge)
