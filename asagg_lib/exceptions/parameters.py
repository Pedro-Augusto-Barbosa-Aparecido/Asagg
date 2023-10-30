class InsuficientLenghtOfParametersList(Exception):
    """
    Indicates that numbers of parameters is invalid

    ```python
    >>> def foo(*args):
    >>>    if len(args) < 2:
    >>>       raise InsuficientLenghtOfParametersList()
    ```

    """

    ...
