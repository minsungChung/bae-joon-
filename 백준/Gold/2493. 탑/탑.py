import sys

input = sys.stdin.readline

n = int(input().rstrip())
tops = list(map(int, input().rstrip().split()))
answer = [0 for _ in range(n)]
stack = [n-1]

for i in range(n-2, -1, -1):
    while len(stack) and tops[stack[-1]] < tops[i]:
        j = stack.pop()
        answer[j] = i+1
    stack.append(i)

print(' '.join(map(str, answer)))