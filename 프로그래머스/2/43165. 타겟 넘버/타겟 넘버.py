def solution(numbers, target):
    answer = [0]
    
    def dfs(cur, i):
        if i == len(numbers):
            if cur == target:
                answer[0] += 1
            return
        
        dfs(cur+numbers[i], i+1)
        dfs(cur-numbers[i], i+1)
            
    dfs(0, 0)
    
    return answer[0]