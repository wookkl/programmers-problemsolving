def solution(s):
    s=list(s)
    stack=[]
    while s:
        stack.append(s.pop())
        while s and stack and stack[-1]==s[-1]:
            stack.pop()
            s.pop()
    if stack: return 0
    else: return 1
