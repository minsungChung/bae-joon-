
if __name__ == '__main__':
    n = int(input())
    moneys = list(map(int, input().split()))
    total = int(input())
    if total >= sum(moneys):
        print(max(moneys))
    else:
        moneys.sort()
        cnt = n
        while True:
            check = True
            avg = total / cnt
            for i in range(n-cnt, n):
                if moneys[i] < avg:
                    total -= moneys[i]
                    cnt -= 1
                    check = False

            if check:
                print(int(avg))
                break










