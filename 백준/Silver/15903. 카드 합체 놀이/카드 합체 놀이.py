import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
card_lst = list(map(int, input().rstrip().split()))
heapq.heapify(card_lst)

for _ in range(m):
    a = heapq.heappop(card_lst)
    b = heapq.heappop(card_lst)
    s = a+b
    heapq.heappush(card_lst, s)
    heapq.heappush(card_lst, s)

print(sum(card_lst))

