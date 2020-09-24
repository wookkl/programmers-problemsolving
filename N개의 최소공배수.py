from math import gcd
def lcm(a,b):
    return (a*b)//(gcd(a,b))
def solution(arr):
    l=arr[0]
    for i in arr[1:]:
        l=lcm(l,i)
    return l