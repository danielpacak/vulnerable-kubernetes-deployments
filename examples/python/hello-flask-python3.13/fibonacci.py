def fibonacci(n: int) -> int:
    if n < 2:  # base case
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)  # recursive case
