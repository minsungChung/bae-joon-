import sys
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    numbers = []
    n = int(input().rstrip())
    flag = True
    for i in range(n):
        num = input().rstrip()
        numbers.append(num)

    numbers.sort()

    for i in range(n-1):
        compare = numbers[i+1][:len(numbers[i])]
        if numbers[i] == compare:
            flag = False
            print('NO')
            break


    if flag:
        print('YES')