
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
edges = []

for _ in range(m):
    edges.append(tuple(map(int, input().rstrip().split())))

edges.sort(key=lambda x: x[2])

parent = list(range(n+1))
num_edge = 0
answer = 0
def find_parent(x):
    if parent[x] == x:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]

def addEdge(x, y):
    root_x = find_parent(x)
    root_y = find_parent(y)
    if root_x > root_y:
        parent[root_x] = root_y
    else:
        parent[root_y] = root_x

for idx, adj, cost in edges:
    if n == 2:
        break
    if find_parent(idx) != find_parent(adj):
        addEdge(idx, adj)
        answer += cost
        num_edge += 1
        if num_edge == n-2:
            break
            
print(answer)
