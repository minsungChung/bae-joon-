a, b = map(int, input().split())
tile = []
min_ = 2500
for i in range(a):
    tile.append(input())

for m in range(a-7):
    for n in range(b-7):
        first_b = 0
        first_w = 0
        for i in range(m, m+8):
            for j in range(n, n+8):
                if (i+j)%2 == 0:
                    if tile[i][j] == 'W':
                        first_b += 1
                    else:
                        first_w += 1
                else:
                    if tile[i][j] == 'W':
                        first_w += 1
                    else:
                        first_b += 1
        min_ = min(min_, min(first_w, first_b))

print(min_)