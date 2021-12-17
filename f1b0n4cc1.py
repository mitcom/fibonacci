# square root of five
V5 = 5 ** 0.5


def f1b(n=None):
    """Yields requested number of Fibonacci sequence if 'n' provided, keep yeling next following terms otherwise

    Assumes the starting values are 0, 1, 1, ...
    Uses the Binet's formula https://en.wikipedia.org/wiki/Fibonacci_number#Closed-form_expression
    F_n\approx \frac{1}{\sqrt{5}}(\frac{1+\sqrt{5}}{2})^{n} https://wikimedia.org/api/rest_v1/media/math/render/svg/0c716b6e2557ea27431203b3c997cfc2166318c6

    But rounding errors after operations on IEEE754 numbers is noticed for values greater than 190392490709135 (70th term),
    so I decided to switch for more common formula since step 70 f(n) = f(n-1) + f(n-2)
    """

    i = 0
    while True:
        if i == n:
            return

        if i <= 69:
            j = int(((1 + V5) / 2) ** i / V5 + 0.5)
            yield j
        elif i == 70:
            k = j + int(((1 + V5) / 2) ** 68 / V5 + 0.5)
            yield k
        else:
            j, k = k, j + k
            yield k

        i += 1
