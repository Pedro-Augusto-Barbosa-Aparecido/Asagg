import unittest

from asagg_lib.exceptions.parameters import InsuficientLenghtOfParametersList
from asagg_lib.utils.list_operations import difference_between_lists


class TestListOperations(unittest.TestCase):
    def setUp(self):
        super(TestListOperations, self).setUp()
        self.list_one = [1, 2, 3, 4, 5]
        self.list_two = [1, 3, 4, 6]

    def test_it_should_be_able_to_get_a_difference_of_to_arrays(self):
        difference = difference_between_lists(self.list_one, self.list_two)

        self.assertEqual(difference, [2, 5, 6])

    def test_it_should_not_be_able_to_get_a_difference_of_only_one_array(self):
        self.assertRaises(
            InsuficientLenghtOfParametersList,
            lambda: difference_between_lists([2]),
        )
