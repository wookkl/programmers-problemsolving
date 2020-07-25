def solution(key, lock):
    answer = True
    plus=len(lock)-1
    plus_list=[0 for _ in range(len(key)+plus*2)]
    for i in range(len(key)):
        for _ in range(plus):
            key[i].insert(0,0)
            key[i].append(0)
    for _ in range(plus):
        key.insert(0,plus_list)
        key.append(plus_list)
    for i in key :
        print(i)
    for _ in range(4):
        for i in range(len(key)-len(lock)+1):
            for j in range(len(key)-len(lock)+1):
                flag =True
                for x in range(len(lock)):
                    for y in range(len(lock)):
                        if lock[x][y] == key[i+x][j+y]:
                            flag=False
                if flag:return True
        lock=rotate(lock)
    return False
def rotate(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N): 
            ret[c][N-1-r] = m[r][c] 
    return ret