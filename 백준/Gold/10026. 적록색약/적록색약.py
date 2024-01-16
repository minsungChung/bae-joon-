import sys
from collections import deque

input = sys.stdin.readline

n = int(input().rstrip())
graph = []
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for _ in range(n):
    graph.append(list(input().rstrip()))

for k in range(2):
    cnt = 0
    visited = [[0] * n for _ in range(n)]
    for l in range(n):
        for j in range(n):
            if not visited[l][j]:
                q = deque([[l, j, graph[l][j]]])
                visited[l][j] = 1
                cnt += 1

                while len(q):
                    y, x, color = q.popleft()

                    for i in range(4):
                        next_y, next_x = y+dy[i], x+dx[i]
                        if 0 <= next_y < n and 0 <= next_x < n:
                            if not visited[next_y][next_x]:
                                if k == 0 and color == graph[next_y][next_x]:
                                    visited[next_y][next_x] = 1
                                    q.append([next_y, next_x, color])
                                elif k == 1 and (color == graph[next_y][next_x] or (color == 'R' and graph[next_y][next_x] == 'G') or (color == 'G' and graph[next_y][next_x] == 'R')):
                                    visited[next_y][next_x] = 1
                                    q.append([next_y, next_x, color])

    print(cnt, end=" ")