import sys
input = sys.stdin.readline

N, M = map(int, input().split())
books = list(map(int, input().split()))
res = 0

if N == 1:
    print(abs(books[0]))
else:
    less_zero = []
    bigger_zero = []

    for book in books:
        if book < 0:
            less_zero.append(book)
        else:
            bigger_zero.append(book)

    less_zero.sort()
    bigger_zero.sort()

    def get_counts(lst):
        answer = 0
        # 오른쪽 절대값이 더 크면 왼쪽부터 책 놓기
        if lst[0] < 0:
            i = 0
            while i+M <= len(lst)-1:
                answer += abs(lst[i]*2)
                i += M
            if i <= len(lst)-1:
                answer += abs(lst[i]*2)
        else:
            i = len(lst)-1
            while i-M >= 0:
                answer += abs(lst[i]*2)
                i -= M
            if i >=0 :
                answer += abs(lst[i]*2)
        return answer

    if less_zero and bigger_zero:
        res += get_counts(less_zero)
        res += get_counts(bigger_zero)
        res -= max(abs(less_zero[0]), bigger_zero[-1])
    elif less_zero:
        res += get_counts(less_zero)
        res -= abs(less_zero[0])
    elif bigger_zero:
        res += get_counts(bigger_zero)
        res -= abs(bigger_zero[-1])


    print(res)