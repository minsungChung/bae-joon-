from collections import deque
import sys

input = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, input().split())
    pop_list = list(map(int, input().split()))
    q = deque([i for i in range(1, n+1)])
    answer = 0
    for num in pop_list:
        if q.index(num) <= len(q)//2:
            while q[0] != num:
                q.append(q.popleft())
                answer += 1
        else:
            while q[0] != num:
                q.appendleft(q.pop())
                answer += 1
        q.popleft()
    print(answer)



