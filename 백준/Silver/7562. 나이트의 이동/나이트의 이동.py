import sys
from collections import deque

input = sys.stdin.readline

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

t = int(input().rstrip())
for _ in range(t):
    l = int(input().rstrip())
    cur_y, cur_x = map(int, input().rstrip().split())
    fin_y, fin_x = map(int, input().rstrip().split())
    visited = [[0] * l for _ in range(l)]
    total = 0

    q = deque([[cur_y, cur_x, 0]])
    visited[cur_y][cur_x] = 1
    while len(q):
       y, x, cnt = q.popleft()

       if x==fin_x and y==fin_y:
           print(cnt)
           break

       for i in range(8):
           if 0 <= x+dx[i] < l and 0 <= y + dy[i] < l and not visited[y+dy[i]][x+dx[i]]:
               visited[y+dy[i]][x+dx[i]] = 1
               q.append([y+dy[i], x+dx[i], cnt+1])