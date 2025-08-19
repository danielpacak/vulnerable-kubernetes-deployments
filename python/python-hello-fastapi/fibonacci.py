def fibonacci(n: int) -> int:
    """
    The slowest possible way to calculate fibonacci numbers.
    :param n: xxx
    :return: yyy
    """
    if n < 2:  # base case
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)  # recursive case
