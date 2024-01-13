
import sys
input = sys.stdin.readline

n = int(input().rstrip())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
edges = []

for i in range(n-1):
    for j in range(i+1, n):
        edges.append([i, j, graph[i][j]])

edges.sort(key=lambda x:x[2])
parent = list(range(n))
num_edges = 0
answer = 0
def find_parent(x):
    if parent[x] == x:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]

def addEdge(x, y):
    root_x = find_parent(x)
    root_y = find_parent(y)
    if root_y > root_x:
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y

for idx, adj, cost in edges:
    if find_parent(idx) != find_parent(adj):
        addEdge(idx, adj)
        answer += cost
        num_edges += 1
        if num_edges == n-1:
            break
            
print(answer)