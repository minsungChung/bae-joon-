import sys

input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
dic = {i: [] for i in range(1, n+1)}
visited = [0 for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, input().rstrip().split())
    dic[s].append(e)
    dic[e].append(s)

def dfs(s):
    for i in dic[s]:
        if visited[i-1] == 0:
            visited[-1] += 1
            visited[i-1] = 1
            dfs(i)

dfs(1)
print(0 if n == 1 else visited[-1]-1)

