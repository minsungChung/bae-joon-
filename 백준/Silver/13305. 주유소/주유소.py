
if __name__ == '__main__':
    n = int(input())
    weight = list(map(int, input().split()))
    nodes = list(map(int, input().split()))
    nodes[-1] = 0
    answer = 0
    curr = 0
    while True:
        if curr == n-1:
            print(answer)
            break
        w = 0
        cnt = 0
        for i in range(curr+1, n):
            w += weight[i-1]
            if nodes[curr] >= nodes[i]:
                answer += nodes[curr] * w
                curr += cnt + 1
                break
            else:
                cnt += 1










