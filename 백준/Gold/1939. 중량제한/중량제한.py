import collections
import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
graph = collections.defaultdict(list)

for _ in range(M):
    s, e, c = map(int, input().split())
    graph[s].append([e, c])
    graph[e].append([s, c])


start, end = map(int, input().split())

h = [[-float('inf'), end]]
visited = set()
answer = 0
while h:
    cost, node = heapq.heappop(h)

    if node == start:
        answer = max(answer, -cost)

    if node not in visited:
        visited.add(node)
        for no, co in graph[node]:
            heapq.heappush(h, [max(cost, -co), no])

print(answer)

