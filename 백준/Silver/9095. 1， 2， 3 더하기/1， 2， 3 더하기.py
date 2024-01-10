import sys
input = sys.stdin.readline

n = int(input().rstrip())
lst = [1, 2, 3]

for _ in range(n):
    num = int(input().rstrip())
    answer = [0]
    def dfs(_sum, goal):
        if _sum > goal:
            return

        if _sum == goal:
            answer[0] += 1
            return

        for number in lst:
            dfs(_sum+number, goal)

    dfs(0, num)
    print(answer[0])