def dfs(x,y,vstd,nodes):
    stack=[[x,y]]
    vstd[x][y]=True
    while stack:
        i,j=stack.pop()
        for a,b in nodes:
            if not vstd[a][b] and j==a:
                stack.append([a,b])
                vstd[a][b]=True

def solution(n, computers):
    answer = 0
    nodes=[]
    vstd=[[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j]and not [i,j] in nodes:
                nodes.append([i,j])
                nodes.append([j,i])
    for i in range(n):
        for j in range(n):
            if [i,j] in nodes and not vstd[i][j]:
                dfs(i,j,vstd,nodes)
                answer+=1
    return answer