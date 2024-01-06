import sys

input = sys.stdin.readline

n = int(input().rstrip())
for _ in range(n):
    kinput = input().rstrip()
    stack1 = []
    stack2 = []
    for k in kinput:
        if k == '<' and len(stack1) > 0:
            stack2.append(stack1.pop())
        elif k == '>' and len(stack2) > 0:
            stack1.append(stack2.pop())
        elif k == '-' and len(stack1) > 0:
            stack1.pop()
        elif k not in ['<', '>', '-']:
            stack1.append(k)

    print(''.join(stack1)+''.join(stack2[::-1]))


