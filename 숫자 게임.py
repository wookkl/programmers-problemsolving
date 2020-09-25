def solution(A, B):
    result=len(A)
    A.sort(reverse=True);B.sort(reverse=True)
    while B:
        b=B.pop()
        if A[-1] < b:
            A.pop()
    return result - len(A)