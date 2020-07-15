def solution(routes):
    cnt=0
    routes = sorted(routes,key = lambda x : x[1],reverse=True)
    while routes:
        st,en=routes.pop()
        for i in reversed(range(len(routes))):
            if routes[i][0]<= en <= routes[i][1]:
                routes.pop(i)
        cnt+=1
    return cnt