def solution(s):
    answer=1
    _len=len(s)
    if _len == 1: return answer
    idx = 0
    while idx < _len:
        if idx+1 <_len and s[idx-1]==s[idx+1]:
            sub=0
            while idx+sub<_len and idx-sub>=0:
                if s[idx-sub]==s[idx+sub]:
                    sub+=1
                else:
                    break
            answer = max(answer,(sub-1)*2+1)
        if s[idx-1]==s[idx]:
            sub=0
            while idx+sub<_len and idx-sub>=0:
                if s[idx-sub-1]==s[idx+sub]:
                    sub+=1
                else:
                    break
            answer = max(answer,(sub)*2)
        idx+=1
    return answer