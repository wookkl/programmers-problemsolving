def solution(n, works):
    time,l,r = 0,0,max(works)
    while l + 1 < r:
        mid= (l+r)//2
        s=0
        for i in works:
            s+= (i - mid) if i - mid>0 else 0
        if s < n:
            r = mid
        else:
            l = mid
    for i in works:
        time+=(i-l) if i-l > 0 else 0
    if time < n:
        return 0
    elif time == n:
        return sum([ pow(l,2) if works[i] >= l else pow(works[i],2) for i in range(len(works)) ])
    else:
        dif=time - n
        res =[]
        for _ in range(dif):
            res.append(l+1)
        for i in works:
            if i < l:
                res.append(i)
        for _ in range(len(works)-len(res)):
            res.append(l)
        return sum([pow(i,2) for i in res])
