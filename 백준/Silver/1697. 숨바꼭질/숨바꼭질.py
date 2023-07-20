from collections import deque

if __name__ == '__main__':
    n, k = map(int, input().split())
    q = deque([[n, 0]])

    visited = [0]*100001

    while True:
        pos, time = q.popleft()
        visited[pos] = 1

        if pos == k :
            print(time)
            break

        if pos-1 >= 0 and visited[pos-1] == 0:
            q.append([pos-1, time+1])
        if pos+1 <= 100000 and visited[pos+1] == 0:
            q.append([pos+1, time+1])
        if pos*2 <= 100000 and visited[pos*2] == 0:
            q.append([pos*2, time+1])








