import sys
if __name__ == '__main__':
    input = sys.stdin.readline

    # 메모장 단어 개수, 블로그 글 개수
    n, m = map(int, input().rstrip().split())
    answer = n
    dict = {}
    for _ in range(n):
        dict[input().rstrip()] = 0

    for _ in range(m):
        blogs = list(input().rstrip().split(','))
        for w in blogs:
            if w in dict.keys() and dict[w] == 0:
                dict[w] = 1
                answer -= 1

        print(answer)








