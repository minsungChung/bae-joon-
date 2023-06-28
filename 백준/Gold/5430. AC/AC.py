from collections import deque

if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        p = input()
        x = int(input())
        lst = input()
        if x != 0:
            lst = lst[1:-1]
            lst = list(lst.split(','))
            q = deque(lst)
        else :
            q = deque()
        reverse = -1
        check = 0

        for i in p:
            if i == 'R':
                reverse *= -1
            else:
                if len(q) == 0:
                    print('error')
                    check = 1
                    break
                if reverse == -1:
                    q.popleft()
                else:
                    q.pop()

        if check == 1:
            continue

        if len(q) == 0:
            print('[]')
            continue

        if reverse == -1:
            lst = list(q)
        else:
            lst = list(q)
            lst.reverse()

        result = '['
        for num in lst:
            result += num + ','

        result = result[:-1] + ']'

        print(result)



