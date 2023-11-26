def check_m(m):
    if m == 0:
        return True
    return False


def solution(n):
    answer = []
    l = [[0 for _ in range(n)] for _ in range(n)]
    num = 1
    cnt = 0
    m = n
    while True:
        for i in range(cnt*2, cnt*2+m):
            l[i][cnt] = num
            num += 1
        m -= 1
        if check_m(m):
            break
        for i in range(m):
            l[n - cnt - 1][cnt + i + 1] = num
            num += 1
        m -= 1
        if check_m(m):
            break
        for i in range(1, m+1):
            l[n - cnt - 1 - i][n-(cnt*2)-i-1] = num
            num += 1
        m -= 1
        if check_m(m):
            break
        cnt += 1

    for i in range(n):
        for j in range(i + 1):
            answer.append(l[i][j])

    return answer