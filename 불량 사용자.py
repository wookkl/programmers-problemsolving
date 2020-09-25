from itertools import permutations
def isBanned(user,ban):
    if len(user)!= len(ban): return False
    for i in range(len(ban)):
        if ban[i] == '*':
            user[i]='*'
    return ban == user
def case(permu,banned_id,n):
    for i in range(n):
        if not isBanned(list(permu[i]),list(banned_id[i])):
            return False
    return True
def solution(user_id, banned_id):
    avail=[]
    result=[]
    for banned in banned_id:
        for user in user_id:
            if not user in avail and isBanned(list(user),list(banned)):
                avail.append(user)
    for permu in permutations(avail,len(banned_id)):
        if case(permu,banned_id,len(permu)):
            if not sorted(list(permu)) in result:
                result.append(sorted(list(permu)))
    
    return len(result)