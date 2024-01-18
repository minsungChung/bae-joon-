import sys
import heapq
input = sys.stdin.readline

N = int(input())
lectures = [tuple(map(int, input().rstrip().split())) for _ in range(N)]
lectures.sort(key=lambda x:(x[0], x[1]))
# 각 강의실 종료 시간
classrooms = [0]

for s, e in lectures:
    _min = heapq.heappop(classrooms)
    if s >= _min:
        heapq.heappush(classrooms, e)
    else:
        heapq.heappush(classrooms, _min)
        heapq.heappush(classrooms, e)

print(len(classrooms))