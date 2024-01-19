import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
nums.sort()
_max = int(input())

for i in range(N):
    base = _max // (N-i)
    if nums[i] <= base:
        _max -= nums[i]
    else:
        print(base)
        break
else:
    print(nums[-1])