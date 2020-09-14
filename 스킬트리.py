def solution(skill, skill_trees):
    answer = 0
    skill=list(skill)
    skill_trees = [list(x) for x in skill_trees]
    for tree in skill_trees:
        vstd=[False]*len(skill)
        for sk in tree:
            if sk in skill:
                vstd[skill.index(sk)] = True
                if False in vstd[:skill.index(sk)]:
                    answer+=1
                    break
                    
    return len(skill_trees) - answer