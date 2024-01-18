import sys
import heapq
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    h = list(map(int, input().rstrip().split()))
    heapq.heapify(h)
    total = 0
    for _ in range(n-1):
        a, b = heapq.heappop(h), heapq.heappop(h)
        heapq.heappush(h, a+b)
        total += a+b
    print(total)


