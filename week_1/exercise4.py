import math
from myutils import factorial

def approx_sin(x, n):
    m = 2 * n + 1
    i = 3
    sign = -1
    s = x
    while i <= m:
        s = s + ((sign * math.pow(x, i)) / factorial(i))
        i = i + 2
        sign = -sign
    return s


def approx_cos(x, n):
    m = 2 * n
    i = 2
    sign = -1
    s = 1
    while i <= m:
        s = s + ((sign * math.pow(x, i)) / factorial(i))
        i = i + 2
        sign = -sign
    return s


def approx_sinh(x, n):
    m = 2 * n + 1
    i = 3
    s = x
    while i <= m:
        s = s + (math.pow(x, i) / factorial(i))
        i = i + 2
    return s


def approx_cosh(x, n):
    m = 2 * n
    i = 2
    s = 1
    while i <= m:
        s = s + (math.pow(x, i) / factorial(i))
        i = i + 2
    return s


if __name__ == '__main__':
    x_radian = 0
    print(f"Approximated sin({x_radian}) = {approx_sin(x_radian, 5)}")
    print(f"Approximated cos({x_radian}) = {approx_cos(x_radian, 5)}")
