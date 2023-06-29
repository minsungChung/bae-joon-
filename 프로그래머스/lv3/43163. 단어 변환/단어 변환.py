from collections import deque

def solution(begin, target, words):
    answer = 0
    q = deque([[begin, 0]])
    visited = [0] * len(words)
    
    while q:
        s, cnt = q.popleft()
        
        if s == target:
            answer = cnt
            break
        
        for i in range(len(words)):
            if visited[i] == 0:
                dif = 0
                for j in range(len(s)):
                    if dif > 1:
                        break
                    if s[j] != words[i][j]:
                        dif += 1
                if dif == 1:
                    q.append([words[i], cnt+1])
                    visited[i] = 1
    
    return answer