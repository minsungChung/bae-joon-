import sys
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
edges = []
parent = list(range(n+1))
num_edge = 0
answer = 0

for _ in range(m):
    edges.append(tuple(map(int, input().rstrip().split())))

edges.sort(key=lambda x: x[2])


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def addEdge(x, y):
    root_x = find(x)
    root_y = find(y)
    parent[root_y] = root_x



for idx, adj, cost in edges:
    if find(idx) != find(adj):
        addEdge(idx, adj)
        answer += cost
        num_edge += 1
        if num_edge == n-1:
            break

print(answer)