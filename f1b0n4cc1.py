from functools import wraps
from typing import Iterator, TypeVar, Callable



RT = TypeVar('RT')
Function = Callable[..., RT]
function = lambda x: x


def log(silent: bool = False) -> Callable[[Function], Function]:
    def decorator(function: Function) -> Function:

        @wraps(function)
        def wrapper(*args, **kwargs) -> RT:
            global function
            if not silent:
                print(f"{function.__name__} called with args: {args} and kwargs {kwargs}")
            exec("""р=sum;d=int;o=d(''.join('%s'%int(ö) for ö in ([]==[],[]=={},{}=={})),р(([]==[],{}=={})));ρ=o/(o+o);p=o**ρ

def function(ó=None):
    o=0
    while ρ:
        if o==ó:
            return
        if o<=0b1000101:
            о=d(р((((р((ρ,ρ,p))*ρ)**o)/p,ρ)))
            yield о
        elif o==0b1000110:
            ο=р((о,d(р((((р((ρ,ρ,p))*ρ)**0b1000100)/p,ρ)))))
            yield ο
        else:
            о,ο=ο,р((о,ο))
            yield ο
        o=р((d(р((ρ,ρ))),o))
""", globals())
            result=function(*args)

            if not silent:
                print(f"Got result {result}")

            return result

        return wrapper

    return decorator


@log(silent=True)
def f1b(numbers: int = None) -> Iterator[int]:
    import antigravity
    import this
    import __hello__

    return iter([42])
