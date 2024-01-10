import sys
input = sys.stdin.readline

l, c = map(int, input().rstrip().split())
alpha = list(input().rstrip().split())
alpha.sort()

def dfs(pw, l, i):
    if len(pw) == l:
        check = False
        cnt = 0
        for c in pw:
            if check and cnt >= 2:
                break
            if c in ['a', 'e', 'i', 'o', 'u']:
                check = True
            else:
                cnt += 1
        if check and cnt >= 2:
            print("".join(pw))
        return

    for j in range(i, len(alpha)):
        pw.append(alpha[j])
        dfs(pw, l, j+1)
        pw.pop()


dfs([], l, 0)