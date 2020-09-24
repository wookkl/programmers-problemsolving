def solution(s):
    return ' '.join([i[0].upper()+i[1:] if len(i)>1 else i.upper() for i in s.lower().split(' ')])