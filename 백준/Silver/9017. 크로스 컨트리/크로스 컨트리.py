
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        # 팀에 속하지 않는 팀
        not_count = []
        n = int(input())
        rank = list(map(int, input().split()))
        for i in range(1, 201):
            if rank.count(i) == 0:
                break
            if rank.count(i) < 6:
                not_count.append(i)

        teams = [[0, 0] for _ in range(201)]
        score = 0
        for i in range(n):
            if rank[i] not in not_count:
                score += 1
                if teams[rank[i]][1] == 4:
                    teams[rank[i]][1] = score
                elif teams[rank[i]][1] < 4:
                    teams[rank[i]][0] += score
                    teams[rank[i]][1] += 1
        m = 10000000
        answer = 0
        for i in range(1, 201):
            if teams[i][0] != 0:
                if teams[i][0] < m:
                    m = teams[i][0]
                    answer = i
                elif teams[i][0] == m:
                    if teams[i][1] < teams[answer][1]:
                        answer = i

        print(answer)








