import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    scores = [tuple(map(int, input().rstrip().split())) for _ in range(n)]
    scores.sort()
    best = scores[0][1]
    answer = 1

    for i in range(1, n):
        if best > scores[i][1]:
            answer += 1
            best = scores[i][1]

    print(answer)