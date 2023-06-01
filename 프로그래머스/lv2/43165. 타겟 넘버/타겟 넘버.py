def solution(numbers, target):
    answer = 0
    total = len(numbers)
    sum1 = 0
    
    def dfs(start, target, sum1):

        nonlocal answer
        
        if start == total:
            if sum1 == target:
                answer += 1
            return
                
        dfs(start+1, target, sum1+numbers[start])
        dfs(start+1, target, sum1-numbers[start])
        
    
    dfs(0, target, sum1)
        
                
            
    return answer
        
    
    dfs(0, total, sum1)
        
                
            
    return answer