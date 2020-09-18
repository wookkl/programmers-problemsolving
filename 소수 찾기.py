from itertools import permutations
def isPrime(a):
    if a < 2:
        return False
    for i in range(2,a):
        if(a%i==0):
            return False
    return True

def solution(numbers):
    numbers = list(numbers)
    l=[]
    for i in range(1,len(numbers)+1):
        l.extend(permutations(numbers,i))
    for i in range(len(l)):
        l[i] = int("".join(l[i]))
    prime = 0
    for i in set(l):
        if isPrime(i):
            prime+=1
    return prime