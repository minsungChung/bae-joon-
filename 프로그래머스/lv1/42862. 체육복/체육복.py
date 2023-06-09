def solution(n, lost, reserve):
    extra = [0]*(n+1)
    answer = n - len(lost)
    
    for i in reserve:
        extra[i] = 1
    
    for i in lost:
        for j in reserve:
            if i == j:
                extra[i] = 0
                lost[lost.index(i)] = 0
                answer += 1
        
    for i in range(1, n):
        if i in lost:
            if extra[i-1]:
                extra[i-1] = 0
                answer += 1
                
            elif extra[i+1]:
                extra[i+1] = 0
                answer += 1
    
    if n in lost:
        if extra[n-1]:
            answer += 1
                
    return answer