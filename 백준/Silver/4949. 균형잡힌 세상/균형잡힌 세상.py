import sys

input = sys.stdin.readline

s = input().rstrip()

matching = {')': '(', ']': '['}

while s != '.':
    stack = []
    check = True
    for c in s:
        if c in ['(', '[']:
            stack.append(c)
        elif c in [')', ']']:
            if len(stack) and stack[-1] == matching[c]:
                stack.pop()
            else:
                print('no')
                check = False
                break

    if check:
        print('no' if len(stack) else 'yes')

    s = input().rstrip()


