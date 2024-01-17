import sys
input = sys.stdin.readline

n = int(input().rstrip())
nums = []
for _ in range(n):
    nums.append(int(input().rstrip()))

nums.sort()
for num in nums:
    print(num)