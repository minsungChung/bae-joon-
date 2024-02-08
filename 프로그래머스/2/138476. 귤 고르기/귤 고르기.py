import collections

def solution(k, tangerine):
    answer = 0
    dic = collections.defaultdict(int)
    
    for t in tangerine:
        dic[t] += 1
    lst = list(dic.items())
    lst.sort(key=lambda x:-x[1])

    _sum = 0
    for i, cnt in lst:
        _sum += cnt
        answer += 1
        if _sum >= k:
            break
            
    return answer