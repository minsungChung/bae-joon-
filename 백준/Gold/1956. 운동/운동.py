import sys
input = sys.stdin.readline
inf = float('inf')
answer = inf

# 정점의 개수와 간선의 개수
V, E = map(int, input().split())
graph = [[inf] * (V+1) for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u][v] = w

for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for s in range(1, V+1):
    answer = min(answer, graph[s][s])

print(answer if answer != inf else -1)