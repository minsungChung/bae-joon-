def solution(n, times):
    answer = 0
    
    # 최대 시간
    max_times = n * max(times)
    
    s, e, m = 1, max_times, 0
    
    while s <= e:
        m = (s+e)//2
        
        # 심사 가능 명수
        cnt = 0
        
        for t in times:
            cnt += m//t
            
        if cnt < n:
            s = m + 1
        else:
            answer = m
            e = m - 1
            
    return answer