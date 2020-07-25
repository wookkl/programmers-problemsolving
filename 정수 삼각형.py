def solution(triangle):
    dp=[[0 for _ in range(i+1)] for i in range(len(triangle))]
    dp[0]=triangle[0]
    for i in range(1,len(dp)):
        for j in range(i+1):
            if j==0:
                dp[i][j]=triangle[i][j]+dp[i-1][j]
            elif j == len(triangle[i])-1:
                dp[i][j]=triangle[i][j]+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-1])+triangle[i][j]
    return max(dp[-1])