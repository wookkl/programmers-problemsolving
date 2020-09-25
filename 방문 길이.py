dx = [0,0,-1,1]
dy = [-1,1,0,0]
direction={"L":0,"R":1,"D":2,"U":3}

def solution(dirs):
    visit=[]
    curr=[0,0]; dist=0
    dirs=list(dirs[::-1])
    while dirs:
        d = dirs.pop()
        dest = [curr[0]+dx[direction[d]],curr[1]+dy[direction[d]]]
        if not -5<=dest[0]<=5 or not -5<=dest[1]<=5:continue
        route = [curr,dest]
        curr=dest
        if not route in visit :
            visit.append(route)
            visit.append(route[::-1])
            dist+=1
    return dist