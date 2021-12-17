from typing import Iterator


def fib(numbers: int = None) -> Iterator[int]:
    """
    Yields requested numbers of Fibonacci sequence if `numbers` value is provided, keeps yelding an infinite number of consecutive terms otherwise

    Assumes the starting values are 0, 1, 1, ...

    >>> fib() #doctest: +ELLIPSIS
    <generator object fib at 0x...>
    >>> list(fib(0))
    []
    >>> list(fib(1))
    [0]
    >>> list(fib(10))
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """

    if numbers == 0:
        return

    i = 0
    j = 1

    yield i
    yielded = 1

    while True:
        if numbers == yielded:
            return

        yield j
        i, j = j, i + j

        yielded += 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
