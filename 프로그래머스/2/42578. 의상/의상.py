import collections as c

def solution(clothes):
    answer = 1
    dic = c.defaultdict(int)
    
    # 각 종류에 해당하는 아이템 개수 + 1
    for items in clothes:
        dic[items[1]] += 1
        
    # 해당 종류 아이템 개수 + 착용 X 경우    
    for v in dic.values():
        answer *= (v+1)
    
    # 아예 다 안입은건 빼줌
    return answer - 1