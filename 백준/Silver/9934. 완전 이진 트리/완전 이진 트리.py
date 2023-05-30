k = int(input())
nums = list(map(int, input().split()))
tree = [[] for _ in range(k)]

for i in range(k):
    for j in range(2**i-1, len(nums), 2**(i+1)):
        tree[k-1-i].append(nums[j])

for nums in tree:
    for num in nums:
        print(num, end = ' ')
    print()
    