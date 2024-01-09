import sys
from collections import deque

input = sys.stdin.readline

n = int(input().rstrip())
q = deque()

s = set()
answer = 0

for _ in range(n):
    car = input().rstrip()
    q.append(car)

for _ in range(n):
    out_car = input().rstrip()
    # 나갈 순서의 차가 이미 나갔다면
    while q[0] in s:
        q.popleft()

    # 나올 차례가 아닌데 나갔으면 answer += 1 and s에 추가
    if out_car != q[0]:
        answer += 1
        s.add(out_car)
    else:
        q.popleft()

print(answer)


