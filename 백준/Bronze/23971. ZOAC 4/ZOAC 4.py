
if __name__ == '__main__':

    h, w, n, m = map(int, input().split())
    cnt = 1
    if h % (n+1) == 0:
        cnt *= h//(n+1)
    else :
        cnt *= h//(n+1)+1

    if w % (m+1) == 0:
        cnt *= w//(m+1)
    else :
        cnt *= w//(m+1) + 1

    print(cnt)







