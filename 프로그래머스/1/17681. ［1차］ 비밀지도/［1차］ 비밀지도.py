def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        tmp = ""
        for j in range(n):
            a1, a2 = 0, 0
            if arr1[i] > 0:
                a1 = arr1[i] % 2
                arr1[i] //= 2
                
            if arr2[i] > 0:
                a2 = arr2[i] % 2
                arr2[i] //= 2
                
            if a1 or a2:
                tmp += "#"
            else:
                tmp += " "
                    
        tmp = tmp[::-1]
        answer.append(tmp)
    
    return answer