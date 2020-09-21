def solution(s):
    stack=[]
    for i in list(s):
        if i == '(':
            stack.append(i)
        elif i == ')' and stack and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(i)
    if stack: return False
    return True