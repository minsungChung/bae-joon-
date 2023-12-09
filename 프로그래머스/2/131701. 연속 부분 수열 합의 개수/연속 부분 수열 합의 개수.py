def solution(elements):
    answer = 0
    sset = set()
    l = len(elements)
    for i in range(1, l+1):
        for j in range(l):
            if j+i > l :
                sset.add(sum(elements[j:] + elements[:j+i-l]))
            else:
                sset.add(sum(elements[j:j+i]))
                
    answer = len(sset)
    return answer