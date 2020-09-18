def solution(number, k):
    number = list(number)[::-1]
    left,right=len(number)-2,len(number)-1
    cnt=k
    while cnt:
        if number[left] > number[right]:
            del number[right]
            if len(number)-1 < right:
                right-=1
                left-=1
            cnt-=1
        else:
            right-=1
            left-=1
    return ''.join(number[::-1])