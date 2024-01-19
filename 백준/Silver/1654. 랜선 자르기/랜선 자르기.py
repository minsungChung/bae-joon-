import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]
left, right = 0, max(lines)
answer = 0

while left <= right:
    mid = (left+right) // 2
    make = 0
    
    if not mid:
        break

    for line in lines:
        make += line//mid
        if make >= N:
            break

    else:
        right = mid-1
        continue
    left = mid+1

print(right)

