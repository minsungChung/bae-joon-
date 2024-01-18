import sys
input = sys.stdin.readline

N = int(input())
meetings = [tuple(map(int, input().rstrip().split())) for _ in range(N)]
# 끝나는 시간에 맞춰서 정렬 -> 빨리 끝나야 다른 회의를 더 할 수 있으니까
meetings.sort(key=lambda x:(x[1], x[0]))

answer = 0
pre_end = 0

for start, end in meetings:
    if start >= pre_end:
        answer += 1
        pre_end = end

print(answer)