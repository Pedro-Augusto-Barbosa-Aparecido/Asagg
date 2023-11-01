from asagg_lib.exceptions.parameters import InsuficientLenghtOfParametersList


def difference_between_lists(*arrays: list) -> list:
    """
    This function get diference between lists and return dijoint elements of lists

    Parameters:
        *arrays: list of lists that's you want extract dijoint elements

    Returns:
        List of a dijoint elements of passed lists

    Examples:
        >>> difference_between_lists([1, 3, 3, 2], [1, 3, 4])
        [2, 4]
    """
    if len(arrays) < 2:
        raise InsuficientLenghtOfParametersList()

    difference = arrays[0]
    for array in arrays[1:]:
        _d = set(difference) ^ set(array)
        difference = list(_d)
    return list(difference)
