import math


def digits(n):
    return 1 if n == 0 else math.floor(math.log(n, 10)) + 1
