def solution(brown, yellow):
    answer = []
    block = brown + yellow
    hor = 3

    while True:
        if block/hor  ==  block // hor:
            ver = block //hor 
            brown_block = hor * 2 + ver * 2 - 4
            yellow_block = (hor -2) * (ver -2)
            if [brown,yellow] == [brown_block,yellow_block]:
                return sorted([ver,hor],reverse=True)
        hor+=1
    return answer
print(solution(10,2))