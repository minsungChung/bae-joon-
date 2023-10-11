n, m = map(int, input().split())

pair = []

def btracking(n, m, pair):
    if len(pair) == m :
        print(' '.join(map(str,pair)))
        return

    for i in range(1, n+1):
        if i not in pair:
            pair.append(i)
            btracking(n, m, pair)
            pair.pop()

btracking(n, m, pair)
