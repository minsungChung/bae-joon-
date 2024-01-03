
import sys

stack = []

def push(num):
    stack.append(num)

def pop():
    if len(stack) == 0:
        return -1
    n = stack.pop()
    return n
    


n = int(sys.stdin.readline().rstrip())

for i in range(n):
    s = sys.stdin.readline().rstrip()
    stack = []
    for ch in s:
        if ch == '(':
            push(1)
        if ch == ')':
            result = pop()
            if result == -1:
                stack.append(1)
                break

    if len(stack) == 0:
        print("YES")
    else :
        print("NO")
            