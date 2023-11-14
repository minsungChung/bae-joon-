def solution(n):
    answer = []
    
    def hanoi(n, fr, to, aux):
        if n == 1:
            answer.append([fr, to])
            return
        
        hanoi(n-1, fr, aux, to)
        answer.append([fr, to])
        hanoi(n-1, aux, to, fr)
        
    hanoi(n, 1, 3, 2)

    
    return answer