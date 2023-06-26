import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while True:
        m1 = heapq.heappop(scoville)
        if m1 >= K:
            break
            
        if len(scoville) == 0:
            answer = -1
            break
            
        m2 = heapq.heappop(scoville)
        heapq.heappush(scoville, m1 + m2*2)
        answer += 1
        
    return answer