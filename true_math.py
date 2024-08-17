# Если делим на 0, то возвращается inf (знак бесконечности)
from math import inf


def divide(first, second):
    if second == 0:
        return inf
    else:
        return first / second
