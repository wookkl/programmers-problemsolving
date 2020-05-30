def solution(N):
    tile=[0,1]
    if N == 1 : return 4
    for i in range(2,N+1):
        tile.append(tile[i-1]+tile[i-2])
    return 4*tile[N] + 2*tile[N-1]