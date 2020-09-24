def solution(n):
    c = list(str(bin(n))).count('1')
    while True:
        n+=1
        if c == list(str(bin(n))).count('1'):
            return n