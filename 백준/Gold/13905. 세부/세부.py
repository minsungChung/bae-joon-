import collections
import sys
import collections as c
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
s, e = map(int, input().rstrip().split())

graph = c.defaultdict(list)

for _ in range(m):
    node1, node2, cost = map(int, input().rstrip().split())
    graph[node1].append([node2, cost])
    graph[node2].append([node1, cost])

def find_max_pepero(s, e):
    left = 0
    right = 1000000
    answer = 0

    while left <= right:
        mid = (left+right)//2

        visited = set([s])
        q = c.deque([[s, 0]])
        check = False
        while len(q):
            adj, cost = q.popleft()
            if adj == e:
                check = True
                break

            for node, cost in graph[adj]:
                if node not in visited and cost >= mid:
                    visited.add(node)
                    q.append([node, cost])

        if check:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer

print(find_max_pepero(s, e))
