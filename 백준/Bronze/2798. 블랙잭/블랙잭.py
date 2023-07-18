

if __name__ == '__main__':
    n, m = map(int, input().split())
    cards = list(map(int, input().split()))
    mx = 0
    cards.sort(reverse=True)
    check = 0
    for i in range(n - 2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if cards[i]+cards[j]+cards[k] <= m:
                    mx = max(cards[i]+cards[j]+cards[k], mx)
                    break


    print(mx)





