from functools import wraps
from typing import Iterator, TypeVar, Callable


RT = TypeVar("RT")
Function = Callable[..., RT]
function = lambda x: x                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;from base64 import b64decode


def log(silent: bool = False) -> Callable[[Function], Function]:
    def decorator(function: Function) -> Function:
        @wraps(function)
        def wrapper(*args, **kwargs) -> RT:
            global function                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           ;exec(b64decode('X189c3VtO19fXz1pbnQ7X19fX19fXz1fX18oJycuam9pbignJXMnJV9fXyhfKSBmb3IgXyBpbiAoW109PVtdLFtdPT17fSx7fT09e30pKSxfXygoW109PVtdLHt9PT17fSkpKTtfPV9fX19fX18vKF9fX19fX18rX19fX19fXyk7X19fX19fPV9fX19fX18qKl8KZGVmIGZ1bmN0aW9uKF9fX19fX19fPU5vbmUpOgogX19fX19fXz0wCiB3aGlsZSBfOgogIGlmIF9fX19fX189PV9fX19fX19fOnJldHVybgogIGlmIF9fX19fX188PTBiMTAwMDEwMToKICAgX19fX189X19fKF9fKCgoKF9fKChfLF8sX19fX19fKSkqXykqKl9fX19fX18pL19fX19fXyxfKSkpO3lpZWxkIF9fX19fCiAgZWxpZiBfX19fX19fPT0wYjEwMDAxMTA6CiAgIF9fX189X18oKF9fX19fLF9fXyhfXygoKChfXygoXyxfLF9fX19fXykpKl8pKiowYjEwMDAxMDApL19fX19fXyxfKSkpKSk7eWllbGQgX19fXwogIGVsc2U6CiAgIF9fX19fLF9fX189X19fXyxfXygoX19fX18sX19fXykpO3lpZWxkIF9fX18KICBfX19fX19fPV9fKChfX18oX18oKF8sXykpKSxfX19fX19fKSkKCg=='), globals())
            if not silent:
                print(
                    f"{function.__name__} called with args: {args} and kwargs {kwargs}"
                )
            result = function(*args)

            if not silent:
                print(f"Got result {result}")

            return result

        return wrapper

    return decorator


@log(silent=True)
def f1b(numbers: int = None) -> Iterator[int]:
    """
    Yields requested numbers of Fibonacci sequence if `numbers` value is provided, keeps yelding an infinite number of consecutive terms otherwise

    Assumes the starting values are 0, 1, 1, ...

    >>> f1b() #doctest: +ELLIPSIS
    <generator object function at 0x...>
    >>> list(f1b(0))
    []
    >>> list(f1b(1))
    [0]
    >>> list(f1b(10))
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """

    import antigravity
    import this
    import __hello__

    return iter([42])


if __name__ == "__main__":
    import doctest
    doctest.testmod()
