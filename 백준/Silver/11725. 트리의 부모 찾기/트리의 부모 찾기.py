from collections import deque

n = int(input())
rel = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
q = deque()
visited = [0] * (n+1)

for i in range(n-1):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)



    if a == 1:
        q.append(b)
        rel[b] = 1
        visited[b] = 1
        
    elif b == 1:
        q.append(a)
        rel[a] = 1
        visited[a] = 1




while len(q) != 0:
    root = q.popleft()

    for i in graph[root]:
        if visited[i] == 0:
            q.append(i)
            rel[i] = root
            visited[i] = 1


for i in range(2, n+1):
    print(rel[i])
