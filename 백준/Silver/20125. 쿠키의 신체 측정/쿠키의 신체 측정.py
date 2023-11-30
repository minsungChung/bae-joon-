
if __name__ == '__main__':

    n = int(input())
    pan = [input() for _ in range(n)]
    head = []
    left_arm = 0
    right_arm = 0
    body = 0
    left_leg = 0
    right_leg = 0
    for i in range(n):
        for j in range(n):
            if len(head) == 0 and pan[i][j] == '*':
                head = [i, j]
            elif pan[i][j] == '*' and j < head[1] and i == head[0]+1:
                left_arm += 1
            elif pan[i][j] == '*' and j > head[1] and i == head[0] + 1:
                right_arm += 1
            elif pan[i][j] == '*' and i > head[0] + 1 and j == head[1]:
                body += 1
            elif pan[i][j] == '*' and j < head[1]:
                left_leg += 1
            elif pan[i][j] == '*' and j > head[1]:
                right_leg += 1
    print(head[0]+2, head[1]+1)
    print(left_arm, right_arm, body, left_leg, right_leg)









