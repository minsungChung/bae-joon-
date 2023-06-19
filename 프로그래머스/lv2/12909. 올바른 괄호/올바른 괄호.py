def solution(s):
    answer = True
    
    stack = []
    
    for i in range(len(s)):
        if s[0] == ')':
            answer = False
            break
            
        if s[i] == ')':
            if len(stack) == 0:
                answer = False
                break
            stack.pop()
        else:
            stack.append('(')
            
    if len(stack) > 0:
        answer = False

    return answer