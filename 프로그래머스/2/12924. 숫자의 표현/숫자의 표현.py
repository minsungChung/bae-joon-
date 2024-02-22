def solution(n):
    answer = 1
    
    left, right = 1, 2
    _sum = 1
    
    while left <= right and right <= n:
        if _sum > n:
            _sum -= left
            left += 1
            
        elif _sum < n:
            _sum += right
            right += 1
            
        else:
            answer += 1
            _sum += right
            right += 1
            
    return answer