def solution(land):
    for i in range(1,len(land)):
        for j in range(len(land[0])):
            a=[]
            for x in range(4):
                if x !=j:
                    a.append(land[i-1][x])
            land[i][j]=max(a) + land[i][j]

    return max(land[-1])