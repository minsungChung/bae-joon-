import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))
left, right = 0, 2000000000
answer = 0

while left <= right:
    mid = (left+right) // 2
    bring = 0

    for tree in trees:
        if tree - mid > 0:
            bring += tree-mid
        if bring > M:
            break

    else:
        if bring == M:
            answer = mid
            break
        right = mid-1
        continue

    answer = mid
    left = mid+1


print(answer)