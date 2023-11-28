def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    base = min(len(citations), citations[0])
    
    for i in range(base, 2, -1):
        cnt = 0
        for c in citations:
            if c >= i:
                cnt += 1
            else:
                break
        if cnt >= i:
            answer = i
            break
    
    return answer