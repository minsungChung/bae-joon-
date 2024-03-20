
def solution(number, k):
    answer = []
    l = len(number)
    
    for i in range(l):
        while answer and k > 0 and answer[-1] < number[i]:
            answer.pop()
            k -= 1
            
        answer.append(number[i])
    
    return ''.join(answer[:len(answer)-k])