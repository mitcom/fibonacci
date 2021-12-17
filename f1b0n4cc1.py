V5 = 5 ** 0.5


def f1b(n=None):
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
