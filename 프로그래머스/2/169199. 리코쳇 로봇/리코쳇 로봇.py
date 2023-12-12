from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def solution(board):
    answer = -1
    q = deque()
    height = len(board)
    width = len(board[0])
    visited = [[0 for _ in range(width)] for _ in range(height)]
    for i in range(height):
        for j in range(width):
            if board[i][j] == 'R':
                q.append([i, j, 0])
        if q:
            break

    while q:
        x, y, c = q.popleft()

        # G에 도달한 경우 c 반환
        if board[x][y] == 'G':
            return c

        # 4 방향으로 이동할 수 있는 경우 탐색
        for i in range(4):
            # 원래 위치 복사
            n_x = x
            n_y = y

            # 계속 이동하다가 장애물 걸리거나 벽에 닿으면 스탑
            while 0 <= n_x+dx[i]<height and 0 <= n_y+dy[i]<width and board[n_x+dx[i]][n_y+dy[i]] != 'D':
                n_x += dx[i]
                n_y += dy[i]

            if visited[n_x][n_y] == 0:
                q.append([n_x, n_y, c+1])
                visited[n_x][n_y] = 1
    return answer