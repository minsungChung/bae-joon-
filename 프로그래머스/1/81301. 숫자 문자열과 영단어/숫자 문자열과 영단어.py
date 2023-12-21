def solution(s):
    answer = ''
    start = 0
    tmp = ''
    l = len(s)
    dic = {"one":'1', "two":'2', "three":'3', "four":'4', "five":'5', "six":'6', "seven":'7', "eight":'8', "nine":'9', "zero":'0'}
    while start < l:
        tmp += s[start]
        if tmp in dic.keys():
            answer += dic[tmp]
            tmp = ""
        elif tmp in dic.values():
            answer += tmp
            tmp = ""
        start += 1
        
    answer = int(answer)
    return answer