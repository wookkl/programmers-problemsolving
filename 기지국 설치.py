import math
def solution(n, stations, w):
    idx=0
    stations=stations[::-1]
    answer=0
    while stations:
        loc = stations.pop()
        answer+= math.ceil((loc-w-idx-1)/(2*w+1))
        idx =loc+w
    if idx < n+1:
        answer+= math.ceil((n-idx)/(2*w+1))
    return answer
