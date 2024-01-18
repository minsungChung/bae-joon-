import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
coins = [int(input()) for _ in range(N)]
total = 0
i = N-1

while K:
    if K >= coins[i]:
        cnt = K // coins[i]
        total += cnt
        K -= coins[i]*cnt
    i -= 1

print(total)
