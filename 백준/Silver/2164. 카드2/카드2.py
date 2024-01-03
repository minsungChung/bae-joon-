from collections import deque
def card(n):
    l = [i for i in range(1, n+1)]
    q = deque(l)
    while len(q) > 1:
        q.popleft()
        last = q.popleft()
        q.append(last)
    return q[0]

if __name__ == '__main__':
    print(card(int(input())))



