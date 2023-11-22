def solution(brown, yellow):
    answer = []
    pairs = []
    
    for i in range(1, int(yellow**(1/2)+1)):
        if yellow % i == 0:
            pairs.append([i, yellow//i]);
            
    for p in pairs:
        if (p[0]+p[1]+2)*2 == brown:
            answer = [p[1]+2, p[0]+2]
    return answer