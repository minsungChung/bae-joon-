
if __name__ == '__main__':

    ttt = int(input())

    for _ in range(ttt):
        # 팀의 개수, 문제의 개수, 팀 ID, 로그 엔트리 개수
        n, k, tt, m = map(int, input().split())
        # 팀당 각 문제의 점수
        tests = [[0 for _ in range(k+1)] for _ in range(n+1)]
        tries = [0 for _ in range(n+1)]
        last_entry = [0 for _ in range(n+1)]
        # 최종 점수, 제출한 횟수, 제출 시간
        teams = []
        for k in range(m):
            # 팀ID, 문제 번호, 획득 점수
            i, j, s = map(int, input().split())
            tests[i][j] = max(tests[i][j], s)
            tries[i] += 1
            last_entry[i] = k+1
        for z in range(n+1):
            teams.append([sum(tests[z]), tries[z], last_entry[z], z])

        teams.sort(key=lambda x:(-x[0], x[1], x[2]))
        for w in range(n):
            if teams[w][-1] == tt:
                print(w+1)
                break







