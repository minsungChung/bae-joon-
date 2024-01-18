import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().rstrip().split()))
lst.sort(reverse=True)
answer = 0

for i in range(1, N+1):
    answer += i*lst[i-1]
    
print(answer)