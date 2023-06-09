def solution(clothes):
    answer = 1
    dic = {}
    for item in clothes:
        if item[1] in dic.keys():
            dic[item[1]] += 1
        else:
            dic[item[1]] = 1
    
    for num in dic.values():
        answer *= num+1
        
    answer -= 1
    
    return answer