import sys
import heapq
input = sys.stdin.readline
inf = float('inf')

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

M = 1

while True:
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [[inf] * N for _ in range(N)]

    if N == 0:
        break

    h = [[graph[0][0], 0, 0]]
    visited[0][0] = graph[0][0]

    while h:
        cost, i, j = heapq.heappop(h)

        for k in range(4):
            next_y = i+dy[k]
            next_x = j+dx[k]
            if 0 <= next_x < N and 0 <= next_y < N:
                if visited[next_y][next_x] > cost+graph[next_y][next_x]:
                    visited[next_y][next_x] = cost+graph[next_y][next_x]
                    heapq.heappush(h, [cost+graph[next_y][next_x], next_y, next_x])


    print("Problem %d: %d"% (M, visited[-1][-1]))
    M += 1