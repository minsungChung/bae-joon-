def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]
    def dfs(start, n):
        for i in range(n):
            if visited[i] == 0 and computers[start][i] == 1:
                visited[i] = 1
                dfs(i, n)
        return 1
    
    for i in range(n):
        if visited[i] == 0:
            answer += dfs(i, n)
    
                
    return answer