import sys
import collections as c
import heapq
input = sys.stdin.readline
inf = float('inf')

# 정점의 개수와 간선의 개수
V, E = map(int, input().split())
# 시작 정점
K = int(input())
graph = c.defaultdict(list)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([w, v])

h = [[0, K]]
visited = [inf] * (V+1)
visited[K] = 0

while h:
    cost, node = heapq.heappop(h)

    for co, no in graph[node]:
        if cost+co < visited[no]:
            visited[no] = cost+co
            heapq.heappush(h, [cost+co, no])

for i in range(1, V+1):
    if visited[i] == inf:
        print('INF')
    else:
        print(visited[i])