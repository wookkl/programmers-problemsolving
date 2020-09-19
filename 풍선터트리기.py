def solution(a):
    r= a[::-1]
    left,right=[[False for _ in range(len(a))] for _ in range(2)]
    index=1
    left_min,right_min=[10**9]*2
    for index in range(1,len(a)-1):
        left_min,right_min = min(left_min,a[index-1]),min(right_min,r[index-1])
        if left_min < a[index]:
            left[index]=True
        if right_min < r[index]:
            right[index]=True
    right.reverse()
    cnt=0
    for i in range(len(a)):
        if left[i] and right[i]:cnt+=1
    return len(a) - cnt