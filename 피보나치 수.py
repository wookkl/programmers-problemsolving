def solution(n):
    dp=[1,1]
    for _ in range(n-2):
        dp.append((dp[-1]+dp[-2])%1234567)
    return dp[-1]