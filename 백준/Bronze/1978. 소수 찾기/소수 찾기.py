import math

def is_prime_num(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

a = int(input())
l = list(map(int, input().split()))
cnt = 0
for i in l:
    if is_prime_num(i):
        cnt += 1

print(cnt)
