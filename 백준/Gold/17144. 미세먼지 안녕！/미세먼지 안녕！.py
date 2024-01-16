import sys
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
r, c, t = map(int, input().rstrip().split())
room = []
cleaner = []

for q in range(r):
    row = list(map(int, input().rstrip().split()))
    room.append(row)
    if row[0] == -1:
        cleaner.append(q)

def find_dust():
    dust_lst = []
    for i in range(r):
        for j in range(c):
            if room[i][j] != 0 and room[i][j] != -1:
                dust_lst.append([i, j, room[i][j]])

    return dust_lst

def spread():
    lst = find_dust()
    for y, x, dust in lst:
        for i in range(4):
            next_y = y + dy[i]
            next_x = x + dx[i]
            amount = dust // 5
            if amount == 0:
                continue
            if 0 <= next_y < r and 0 <= next_x < c:
                if room[next_y][next_x] != -1:
                    room[next_y][next_x] += amount
                    room[y][x] -= amount

def upper_clean():
    tmp = 0
    for i in range(cleaner[0]+1):
        if i == 0:
            tmp = room[0][0]
            for j in range(c-1):
                room[0][j] = room[0][j+1]
            room[0][c-1] = room[1][c-1]
        elif i == cleaner[0]:
            for j in range(c-2):
                room[i][c-1-j] = room[i][c-2-j]
            room[i][1] = 0
        else:
            room[i][0], tmp = tmp, room[i][0]
            room[i][c-1] = room[i+1][c-1]

def lower_clean():
    tmp = 0
    for i in range(cleaner[1], r):
        if i == cleaner[1]:
            tmp = room[i][c-1]
            for j in range(c-2):
                room[i][c-1-j] = room[i][c-2-j]
            room[i][1] = 0
        elif i == r-1:
            for j in range(c-1):
                room[r-1][j] = room[r-1][j+1]
            room[r-1][c-1] = tmp
        else:
            room[i][c-1], tmp = tmp, room[i][c-1]
            room[i][0] = room[i+1][0]

for _ in range(t):
    spread()
    upper_clean()
    lower_clean()


answer = 0
for p in range(r):
    answer += sum(room[p])

print(answer+2)


