from math import gcd


def solution(w, h):
    k = gcd(w, h)
    return w * h - ((w + h) // k - 1) * k
