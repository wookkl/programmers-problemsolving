def solution(n, words):
    for i in range(1,len(words)):
        if words[i-1][-1] != words[i][0] or len(words[:i+1]) != len(set(words[:i+1])):
            return [i%n+1,i//n+1]
    return [0,0]