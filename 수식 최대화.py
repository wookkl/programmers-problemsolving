from itertools import permutations
def solution(expression):
    num=''
    answer=[]
    parsed=[]
    for i in list(expression):
        if not i in ['*','-','+']:
            num+=i
        else:
            parsed.append(int(num))
            parsed.append(i)
            num=''
    parsed.append(int(num))
    calc=list(permutations(['*','-','+'],3))
    for cal in calc:
        exp=parsed.copy()
        for c in cal:
            for _ in range(expression.count(c)):
                idx= exp.index(c)
                if c=='+':
                    exp[idx]=int(exp[idx-1])+int(exp[idx+1])
                elif c=='-':
                    exp[idx]=int(exp[idx-1])-int(exp[idx+1])
                else:
                    exp[idx]=int(exp[idx-1])*int(exp[idx+1])
                del exp[idx-1]
                del exp[idx]
        answer.append(abs(exp.pop()))
    return max(answer)
