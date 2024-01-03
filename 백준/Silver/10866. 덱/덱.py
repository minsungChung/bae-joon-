from collections import deque
import sys

input = sys.stdin.readline

if __name__ == '__main__':
    q = deque()
    n = int(input())
    for _ in range(n):
        order = input().split()
        if order[0] == "push_front":
            q.appendleft(int(order[1]))
        elif order[0] == "push_back":
            q.append(int(order[1]))
        elif order[0] == "pop_front":
            print(q.popleft() if len(q) > 0 else -1)
        elif order[0] == "pop_back":
            print(q.pop() if len(q) > 0 else -1)
        elif order[0] == "size":
            print(len(q))
        elif order[0] == "empty":
            print(1 if len(q) == 0 else 0)
        elif order[0] == "front":
            print(q[0] if len(q) > 0 else -1)
        elif order[0] == "back":
            print(q[-1] if len(q) > 0 else -1)




