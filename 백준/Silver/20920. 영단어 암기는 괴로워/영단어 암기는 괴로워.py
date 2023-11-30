
if __name__ == '__main__':
    n, m = map(int, input().split())
    words = []
    dict = {}

    for _ in range(n):
        word = input()
        if len(word) >= m:
            if word in dict.keys():
                dict[word] += 1
            else:
                dict[word] = 1

    for key, value in dict.items():
        words.append([key, value, len(key)])

    words.sort(key=lambda x:(-x[1], -x[2], x[0]))

    for w in words:
        print(w[0])










