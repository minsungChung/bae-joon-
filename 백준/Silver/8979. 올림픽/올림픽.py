

if __name__ == '__main__':

    n, k = map(int, input().split())
    country = []
    place = [[] for _ in range(n)]
    for _ in range(n):
        lst = list(map(int, input().split()))
        country.append(lst)

    country.sort(key=lambda x : (x[1], x[2], x[3]))
    place[0].append(country[0][0])
    p = 0
    for i in range(1, n):
        if country[i][1:] == country[i-1][1:]:
            place[p].append(country[i][0])
        else:
            p += 1
            place[p].append(country[i][0])

    for i in range(n):
        if k in place[i]:
            print(i+1)
            break










