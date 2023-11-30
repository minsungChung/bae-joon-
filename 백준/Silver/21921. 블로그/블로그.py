
if __name__ == '__main__':
    n, x = map(int, input().split())
    visits = list(map(int, input().split()))
    m = 0
    cnt = 0
    s = sum(visits[:x])
    for i in range(n-x+1):
        if i > 0:
            s -= visits[i-1]
            s += visits[i+x-1]
        if s > m:
            m = s
            cnt = 1
        elif s == m :
            cnt += 1

    if m == 0:
        print('SAD')
    else:
        print(m)
        print(cnt)










