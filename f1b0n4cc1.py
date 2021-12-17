from functools import wraps


р=sum
d=int
o=d(''.join('%s'%d(ö) for ö in ([]==[],[]=={},{}=={})),р(([]==[],{}=={})))
ρ=o/(o+o)
p=o**ρ


def log(silent):
    def decorator(function):

        @wraps(function)
        def wrapper(*args, **kwargs):
            if not silent:
                print(f"{function.__name__} called with args: {args} and kwargs {kwargs}")

            result = function(*args, **kwargs)

            if not silent:
                print(f"Got result {result}")

            return result

        return wrapper

    return decorator


@log(silent=False)
def f1b(ó=None):
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
  o=р((ρ,ρ,o))
