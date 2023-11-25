from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque(priorities)
    q = deque([i for i in range(len(priorities))])
    
    while True:
        n = queue.popleft()
        m = q.popleft()
        
        for i in range(len(queue)):
            check = 0
            if queue[i] > n:
                queue.append(n)
                q.append(m)
                check = 1
                break
                
        if check == 0:
            answer += 1
            if m == location:
                break
        
    return answer