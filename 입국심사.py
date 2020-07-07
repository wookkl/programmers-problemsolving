def solution(n, times):
    left=1
    right=10**13
    while(left<=right):
        mid =(left+right)//2
        m=0
        for time in times:
            m+=(mid//time)
        print("전",left,mid,right)
        if m<n:
            left=mid+1
        else:
            right=mid-1
        print("후",left,mid,right)
        print()
    return left