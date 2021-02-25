def solution(N, number):
    dp = [[sum(list(N*10**i for i in range(i)))] for i in range(9)]
    for c in range(2, 9):
        for x in range(1, (c + 1) // 2 + 1):
            for i in dp[x]:
                for j in dp[c-x]:
                    dp[c].append(i + j)
                    dp[c].append(i - j)
                    dp[c].append(i * j)
                    if j and i:
                        dp[c].append(i // j)
                        dp[c].append(j // i)
        dp[c] = list(set(dp[c]))
    for i in range(9):
        if number in dp[i]:
            return i
    return -1
