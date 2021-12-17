It is a clean implementation of Fibonacci sequence iterator ([click here to check the dirty version of the code](../../..)).

> Yields requested numbers of Fibonacci sequence if an argument is provided, keeps yelding an infinite number of consecutive terms otherwise
>
> Assumes the starting values are 0, 1, 1, ... ([according to Wikipedia page](https://en.wikipedia.org/wiki/Fibonacci_number))

## How to use

```py

>>> from fibonacci import fib

>>> fib()
<generator object fib at 0x...>  # an infite generator-iterator

>>> it = fib()
>>> for i in range(5):
...     print(next(it))
...
0
1
1
2
3

>>> for i in fib():
...     print(i)
...     if i > 10:
...         break
...
0
1
1
2
3
5
8
13

>>> list(fib(0))  # it is an empty iterator as zero terms was requested
[]

>>> list(fib(1)) # an iterator wich is exhausted after first requested value
[0]

>>> list(fib(10))
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

## How to test

### Unit tests

```bash
$ python3 test_fibonacci.py
.......
----------------------------------------------------------------------
Ran 7 tests in 0.003s

OK
```

### Doctests

```bash
$ python3 fibonacci.py
```

## How to check types

```bash
$ # python3 -m pip install mypy
$ mypy fibonacci.py
```
