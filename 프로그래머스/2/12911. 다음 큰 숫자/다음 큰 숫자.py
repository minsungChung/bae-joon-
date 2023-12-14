def solution(n):
    answer = 0
    bin_n = []
    cnt = 1
    while n > 1:
        num = n%2
        if num == 1:
            cnt += 1
        bin_n.append(num)
        n //= 2
        
    bin_n.append(1)
    
    cnt1 = 0
    while cnt1 != cnt:
        cnt1 = 0
        up = 1
        for i in range(len(bin_n)):
            if up == 1 and bin_n[i] == 0:
                bin_n[i] = 1
                up = 0
                cnt1 += 1

            elif up == 1 and bin_n[i] == 1:
                bin_n[i] = 0
            
            elif up == 0:
                if bin_n[i] == 1:
                    cnt1 += 1
                
        if up == 1:
            bin_n.append(1)
            cnt1 += 1
            
    for i in range(len(bin_n)):
        answer += bin_n[i] * (2**i)
                
    
    return answer