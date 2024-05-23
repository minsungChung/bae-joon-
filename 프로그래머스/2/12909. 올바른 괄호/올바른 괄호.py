def solution(s):
    answer = True
    stack = []
    
    # '('일 때 집어넣고 ')'일 때 pop
    for p in s:
        if p == '(':
            stack.append('(')
        else:
            # 열린 괄호가 없다면 매칭 X
            if not stack:
                answer = False
                break
            stack.pop()
            
    # 열린 괄호가 남았다면 매칭 X
    if stack:
        answer = False

    return answer