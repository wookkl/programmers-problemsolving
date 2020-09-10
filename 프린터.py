from collections import deque

def IsExist(popped_doc,dq):
    for idx in range(len(dq)):
        if popped_doc < dq[idx][1]:
            return True

def solution(priorities, location):
    dq=[]
    time=1
    for idx,doc in enumerate(priorities):
        dq.append([idx,doc])
    dq = deque(dq)
    while dq:
        popped_idx,popped_doc = dq.popleft()
        if IsExist(popped_doc,dq):
            dq.append([popped_idx,popped_doc])
        else:        
            if popped_idx == location:  
                return time
            else:
                time+=1
print(solution([1,1,9,1,1,1], 0))
        
        