def solution(brown, yellow):
    answer = []
    t = (brown - 4)//2
    
    for i in range(1, t+1):
        if i * (t-i) == yellow:
            if i > t-i:
                answer = [i+2, t-i+2]
            else:
                answer = [t-i+2, i+2]
    
    return answer