
if __name__ == '__main__':
    n = int(input())
    switches = list(map(int, input().split()))
    student_num = int(input())
    students = [list(map(int, input().split())) for _ in range(student_num)]

    for student in students:
        if student[0] == 1:
            for i in range(n):
                if (i+1) % student[1] == 0:
                    switches[i] = 1 if switches[i] == 0 else 0
        else:
            for i in range(student[1]):
                if i == 0:
                    switches[student[1]-1] = 1 if switches[student[1]-1] == 0 else 0

                else:
                    if student[1]+i-1 >= n:
                        break
                    if switches[student[1]+i-1] == switches[student[1]-i-1]:
                        switches[student[1] - i - 1] = 1 if switches[student[1] - i - 1] == 0 else 0
                        switches[student[1] + i - 1] = 1 if switches[student[1] + i - 1] == 0 else 0
                    else:
                        break

    for i in range(n):
        print(switches[i], end = " ")
        if (i+1)%20 == 0:
            print()







