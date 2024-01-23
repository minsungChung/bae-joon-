import sys
import collections as c
import heapq
input = sys.stdin.readline

N, M, X = map(int, input().split())
graph = c.defaultdict(list)

for _ in range(M):
    s, e, c = map(int, input().split())
    graph[s-1].append([e-1, c])

min_costs_going = [0] * N
min_costs_return = [0] * N

for i in range(N):
    if not min_costs_going[i] and i != X-1:
        # cost, node
        h = [[0, i]]
        visited = set()
        while h:
            cost, node = heapq.heappop(h)
            if node == X - 1:
                min_costs_going[i] = cost
                break
            if node not in visited:
                visited.add(node)
                for next, w in graph[node]:
                    if next not in visited:
                        heapq.heappush(h, [cost+w, next])

q = [[0, X-1]]
visited = set()
while q:
    cost, node = heapq.heappop(q)
    if node not in visited:
        visited.add(node)
        min_costs_return[node] = cost

        for next, w in graph[node]:
            if next not in visited:
                heapq.heappush(q, [cost+w, next])

answer = 0
for i in range(N):
    answer = max(answer, min_costs_going[i]+min_costs_return[i])

print(answer)