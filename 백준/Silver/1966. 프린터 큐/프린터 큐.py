from collections import deque
import sys

input = sys.stdin.readline

if __name__ == '__main__':
    T = int(input().rstrip())
    for _ in range(T):
        # 문서 개수, 몇번째 위치
        n, m = map(int, input().rstrip().split())
        priority = list(map(int, input().rstrip().split()))

        q = deque()
        answer = 0
        for i, v in enumerate(priority):
            q.append([i, v])

        priority.sort(reverse=True)

        check = False
        for p in priority:
            while True:
                doc = q.popleft()
                if doc[1] == p:
                    if doc[0] == m:
                        check = True
                    answer += 1
                    break
                else:
                    q.append(doc)
            if check:
                print(answer)
                break





