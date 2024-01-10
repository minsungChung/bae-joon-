import collections as c
import sys
input = sys.stdin.readline

n, m, v = map(int, input().rstrip().split())
dic = c.defaultdict(list)
for _ in range(m):
    node1, node2 = map(int, input().rstrip().split())
    dic[node1].append(node2)
    dic[node2].append(node1)

for key, val in dic.items():
    dic[key] = sorted(val)

visited_dfs = set()
visited_bfs = set()

def dfs(i):
    print(i, end=' ')
    visited_dfs.add(i)
    for j in dic[i]:
        if j not in visited_dfs:
            dfs(j)

def bfs(i):
    q = c.deque([i])
    visited_bfs.add(i)
    while len(q):
        node = q.popleft()
        print(node, end=' ')
        for j in dic[node]:
            if j not in visited_bfs:
                visited_bfs.add(j)
                q.append(j)

dfs(v)
print()
bfs(v)