from asagg_lib.exceptions.parameters import InsuficientLenghtOfParametersList


def difference_between_lists(*arrays: list) -> list:
    if len(arrays) < 2:
        raise InsuficientLenghtOfParametersList()

    difference = arrays[0]
    for array in arrays[1:]:
        _d = set(difference) ^ set(array)
        difference = list(_d)
    return list(difference)
