import heapq
def solution(operations):
    heap = []
    for operation in operations:
        key,number=operation.split(" ")
        number=int(number)
        if key == 'I':
            heapq.heappush(heap, number)
        elif key == 'D' and heap:
            if number == 1:
                heap.pop()
            elif number == -1:
                heapq.heappop(heap)
    if not heap:
        return [0,0]
    
    return [max(heap),heap[0]]
    return answer