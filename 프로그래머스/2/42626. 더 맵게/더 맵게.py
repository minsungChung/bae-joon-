import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while True:
        # 가장 맵지 않은, 두번째로 맵지 않은
        first, second = heapq.heappop(scoville), heapq.heappop(scoville)
        
        # 가장 맵지 않은게 K를 넘으면 모든 음식 스코빌 지수 K 넘음
        if first >= K:
            break
            
        heapq.heappush(scoville, first+second*2)
        answer += 1
        
        # scoville 리스트에 한개가 남았을 때 K보다 작으면 실패
        if len(scoville) == 1:
            if scoville[0] < K:
                answer = -1
            break
        
    return answer