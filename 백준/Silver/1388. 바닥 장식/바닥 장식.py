n, m = map(int, input().split())

visited = [[0 for _ in range(m)] for _ in range(n)]

tiles = []

cnt = 0

for i in range(n):
    tiles.append(list(input()))

for i in range(n):
    for j in range(m):
        if visited[i][j] != 1:
            cur =  tiles[i][j]
            visited[i][j] = 1

        
            if cur == '-':
                k = j
                while True:
              
                    if k == m-1 or tiles[i][k+1] != cur :
                        cnt += 1
                        break
                    visited[i][k+1] = 1
                    k += 1
            else:
                k = i
                while True:
                    if  k == n-1 or tiles[k+1][j] != cur:
                        cnt += 1
                        break
                    visited[k+1][j] = 1
                    k += 1

print(cnt)