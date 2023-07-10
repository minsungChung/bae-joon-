def solution(s):
    answer = []
    tmp = []
    tmp2 = []
    num = ""
    s = s[1:-1]

    for n in s:
        if n == '{':
            cnt = 0
        if n != '{' and n != '}' and n != ',':
            num += n
        if (n == '}' or n == ',') and len(num) > 0:
            cnt += 1
            tmp.append(int(num))
            if n == '}':
                tmp2.append(tmp)
                tmp = []
            num = ''
            
    tmp2.sort(key=lambda x : len(x))

    for i in tmp2:
        for j in i:
            if j not in answer:
                answer.append(j)
            
    return answer