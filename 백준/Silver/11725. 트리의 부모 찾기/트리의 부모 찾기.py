import sys
import collections as c
input = sys.stdin.readline

n = int(input().rstrip())
tree = c.defaultdict(list)
parent = [0 for _ in range(n)]
visited = set()

for _ in range(n-1):
    n1, n2 = map(int, input().rstrip().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

q = c.deque([1])
visited.add(1)
while len(q):
    p = q.popleft()
    for i in tree[p]:
        if i not in visited:
            parent[i-1] = p
            visited.add(i)
            q.append(i)

for i in range(1, n):
    print(parent[i])