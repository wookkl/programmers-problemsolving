import copy
answer=[]
length=0
def dfs(nodes,route):
    global answer
    if len(route) > length:
        answer.append(route)
        return
    if not route[-1] in nodes:
        return
    
    start=route[-1]
    for i in range(len(nodes[start])):
        route.append(nodes[start].pop(i))
        dfs(copy.deepcopy(nodes),copy.deepcopy(route))
        nodes[start].insert(i,route.pop())
def solution(tickets):
    global length
    global answer
    length=len(tickets)
    nodes=dict()
    for start,end in tickets:
        if not start in nodes:
            nodes[start]=[end]
        else:
            nodes[start].append(end)
    for key in nodes:
        nodes[key].sort()
    dfs(nodes,["ICN"])
    answer.sort()
    return answer[0]