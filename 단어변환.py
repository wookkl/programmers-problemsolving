def cmp(a,b):
    cnt=0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt+=1
    if cnt ==1:
        return True
    else:
        return False
a=[]
def bfs(begin, target, words,vstd,cnt):
    print(vstd)
    for i in range(len(words)):            
        if not vstd[i] and cmp(begin,words[i]):
            if words[i]==target:
                a.append(cnt) 
                return
            vstd[i]=True                
            bfs(words[i],target,words,vstd,cnt+1)
    
def solution(begin, target, words):
    bfs(begin,target,words,[False for _ in range(len(words))],0)
    if not a :
        return 0
    else:
        return min(a)+1