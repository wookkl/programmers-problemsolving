dx=[1,0,-1]
dy=[0,1,-1]
def solution(n):
    if n==1:return [1]
    answer = [[0 for _ in range(x+1)] for x in range(n)]
    s = sum([len(i) for i in answer])
    answer[0][0]=1
    cnt=2
    x,y,mode=0,0,0
    while cnt != s+1:
        if dx[mode]+x==len(answer) or dy[mode]+y == len(answer[dx[mode]+x]) or answer[dx[mode]+x][dy[mode]+y] :
            mode=(mode+1)%3
        answer[dx[mode]+x][dy[mode]+y]=cnt
        x+=dx[mode]
        y+=dy[mode]
        cnt+=1
    ans=[]
    for x in answer:ans.extend(x)
    return ans