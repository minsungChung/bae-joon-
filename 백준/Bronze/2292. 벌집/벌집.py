

if __name__ == '__main__':

    n = int(input())
    e = 1
    cnt = 0
    for i in range(n):
        e += 6*i
        cnt += 1
        if n <= e:
            print(cnt)
            break







