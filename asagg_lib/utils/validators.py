from typing import Any


def validate_type_comparing_with_annother_var(
    type_to_compare: Any, value_that_will_be_compared: Any
) -> bool:
    """
    Check if the value is the same instance or the subclass is the same, that is, it compares whether
    it is possible to perform the implicit casting of python

    Parameters:
        type_to_compare: type to compare with the value
        value_that_will_be_compared: value that's you want convert

    Returns:
        return True if value is castable or false otherwise
    """

    # comparing if both values is the same type
    if isinstance(value_that_will_be_compared, type_to_compare):
        return True
    return False
