import unittest

from asagg_lib.utils.validators import validate_type_comparing_with_annother_var


class TestValidator(unittest.TestCase):
    def setUp(self):
        super(TestValidator, self).setUp()

    def test_it_should_be_able_to_return_true_when_an_object_is_instance_of_some_type(
        self,
    ):
        is_valid_value = validate_type_comparing_with_annother_var(int, 2)

        self.assertTrue(is_valid_value)

    def test_it_should_be_able_to_return_false_when_an_object_is_instance_of_some_type(
        self,
    ):
        is_valid_value = validate_type_comparing_with_annother_var(
            int, "String"
        )

        self.assertFalse(is_valid_value)
