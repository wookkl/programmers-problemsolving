from itertools import combinations
from math import sqrt
def isPrime(n):
    for i in range(2,int(sqrt(n))+1):
        if not n % i:
            return False
    return True
def solution(nums):
    return len([True for i in combinations(nums,3) if isPrime(sum(i))])
