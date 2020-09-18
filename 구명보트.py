from collections import deque
def solution(people, limit):
    people = deque(sorted(people))
    boat=0
    while people:
        if len(people) >1:
            if people[0] + people[-1] <= limit:
                boat+=1
                people.popleft();people.pop()
            else:
                people.pop()
                boat+=1
        else:
            boat+=1
            break
    return boat