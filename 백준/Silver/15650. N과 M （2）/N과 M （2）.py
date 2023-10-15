
if __name__ == '__main__':
    def solution(n, m, pair, k):

        if len(pair) == m:
            print(' '.join(map(str, pair)))

        for i in range(k, n+1):
            if i not in pair:
                pair.append(i)
                solution(n, m, pair, i+1)
                pair.pop()

    n, m = map(int, input().split())

    solution(n, m, [], 1)








