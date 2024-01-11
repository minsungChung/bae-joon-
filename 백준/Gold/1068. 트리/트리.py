import sys
import collections as c
input = sys.stdin.readline

n = int(input().rstrip())
tree = c.defaultdict(list)
lst = list(map(int, input().rstrip().split()))
want_delete = int(input().rstrip())
root = -1

for i in range(n):
    if lst[i] == -1:
        root = i
    elif i != want_delete and lst[i] != want_delete:
        tree[i].append(lst[i])
        tree[lst[i]].append(i)

q = c.deque([root])
answer = 0
visited = set()
visited.add(root)
while len(q):
    node = q.popleft()
    # 연결된게 부모밖에 없으면 즉 리프노드이면
    if node != root and len(tree[node]) == 1:
        answer += 1
    else:
        for child in tree[node]:
            if child not in visited:
                visited.add(child)
                q.append(child)

print(1 if not len(tree[root]) and want_delete != root else answer)


