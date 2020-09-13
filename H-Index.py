def solution(citations):
    citations.sort()
    for i in range(1000,0,-1):
        quotation,remainder=0,0
        for quote in citations:
            if quote >= i :
                quotation+=1
            if quote <= i :
                remainder+=1
        if quotation >= i and remainder<=i:
            return i
    return 0