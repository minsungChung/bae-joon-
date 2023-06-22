def solution(numbers):
    answer = ''
    tmp = []
    for num in numbers:
        if num < 10:
            tmp.append([str(num)*12, 1])
        elif num < 100:
            tmp.append([str(num)*6, 2])
        elif num < 1000:
            tmp.append([str(num)*4, 3])
        else:
            tmp.append([str(num)*2, 4])
            
    tmp.sort(reverse=True)
    
    for i in range(len(tmp)):
        answer += tmp[i][0][:tmp[i][1]]
    if int(answer) == 0:
        answer = '0'
    return answer