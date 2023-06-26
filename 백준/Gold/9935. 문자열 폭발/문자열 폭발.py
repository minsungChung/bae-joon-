original = input()
bomb = input()
stack = []

for c in original:
    check = 0
    stack.append(c)
    if c == bomb[-1]:
        for i in range(len(bomb)):
            if len(stack)-len(bomb) < 0:
                check = 1
                break
            if stack[len(stack)-len(bomb)+i] != bomb[i]:
                check = 1
                break
        if check == 0:
            for i in range(len(bomb)):
                stack.pop()

if len(stack) == 0:
    print('FRULA')
else:
    print(''.join(stack))