from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [0]*(n+1)

for i in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(1, n+1):
    graph[i].sort()

def dfs(graph, v, visited):
    visited[v] = 1
    print(v, end = ' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])

    visited[start] = 1

    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1


dfs(graph, v, visited)
visited = [0]*(n+1)
print()
bfs(graph, v, visited)
