def solution(board, moves):
    answer = 0
    stack = []
    lb = len(board)
    dolls = [[] for _ in range(lb)]
    
    for i in range(lb-1, -1, -1):
        for j in range(lb):
            if board[i][j] != 0:
                dolls[j].append(board[i][j])
                
    for m in moves:
        if len(dolls[m-1]) > 0 :
            doll = dolls[m-1].pop()
            if len(stack) > 0 and stack[-1] == doll :
                answer += 2
                stack.pop()
            else:
                stack.append(doll)
    return answer