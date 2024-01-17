import collections
import sys
input = sys.stdin.readline

N = int(input().rstrip())
nums = []
dic = collections.defaultdict(int)
_sum = 0
for _  in range(N):
    num = int(input().rstrip())
    _sum += num
    dic[num] += 1
    nums.append(num)

nums.sort()
dic_items = list(dic.items())
dic_items.sort(key=lambda x:(-x[1], x[0]))

print(round(_sum/N))
print(nums[N//2])
if N == 1:
    print(nums[0])
else:
    print(dic_items[1][0] if dic_items[0][1] == dic_items[1][1] else dic_items[0][0])
print(nums[-1] - nums[0])
