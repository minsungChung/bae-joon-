def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result
N = int(input())
for i in range(N):
    n, m = map(int, input().split())
    print(factorial(m)//(factorial(m-n)*factorial(n)))
