import sys
import heapq

input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input().rstrip())
    heap = []
    for _ in range(n):
        x = int(input().rstrip())
        if len(heap) == 0 and x == 0:
            print(0)
        elif x == 0:
            print(heapq.heappop(heap))
        else:
            heapq.heappush(heap, x)