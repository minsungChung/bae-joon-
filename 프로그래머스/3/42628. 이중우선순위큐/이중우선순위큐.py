import heapq

def solution(operations):
    answer = []
    heap = []
    for o in operations:
        op, num = o.split()
        if op == 'I':
            heapq.heappush(heap, int(num))
        elif op == 'D' and num == '1':
            if len(heap) == 0:
                continue
            heap.remove(max(heap))
        elif op == 'D' and num == '-1':
            if len(heap) == 0:
                continue
            heapq.heappop(heap)
            
    if len(heap) == 0:
        answer = [0, 0]
    else:
        answer = [max(heap), heapq.heappop(heap)]
    return answer