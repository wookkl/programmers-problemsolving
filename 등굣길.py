def solution(m, n, puddles):
    for i in range(len(puddles)):
        puddles[i].reverse()
    m+=1
    n+=1
    dp=[[0 for _ in range(m) ] for _ in range(n)]
    dp[1][1] = 1
    for i in range(1,n):
        for j in range(1,m):
            if [i,j]==[1,1]:
                continue    
            top = dp[i-1][j] if not [i-1,j] in puddles else 0
            left = dp[i][j-1] if not [i,j-1] in puddles else 0
            if not [i,j] in puddles:
                dp[i][j]=(top+left)%1000000007
    return dp[-1][-1]