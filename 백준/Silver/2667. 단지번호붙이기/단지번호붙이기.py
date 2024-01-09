import sys

input = sys.stdin.readline

n = int(input().rstrip())
grid = []
answer = []
total = 0

for _ in range(n):
    grid.append(list(input().rstrip()))

width = len(grid[0])
height = len(grid)

visited = [[0 for _ in range(width)] for _ in range(height)]
visited.append([0])
def dfs(i, j):
    if i > -1 and i < len(grid) and j > -1 and j < len(grid[0]):
        if grid[i][j] == '1' and visited[i][j] == 0:
            visited[i][j] = 1
            visited[-1][0] += 1
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)

for i in range(height):
    for j in range(width):
        if grid[i][j] == '1' and visited[i][j] == 0:
            dfs(i, j)
            total += 1
            answer.append(visited[-1][0])
            visited[-1][0] = 0

print(total)
answer.sort()
for cnt in answer:
    print(cnt)
