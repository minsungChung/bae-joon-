def solution(numbers):
    answer = ''
    numbers = [str(num) for num in numbers]
    numbers = [[num * (12//len(num)), len(num)] for num in numbers]
    numbers.sort()
    
    for i in range(len(numbers)-1, -1, -1):
        answer += numbers[i][0][:numbers[i][1]]
    
    return '0' if int(answer)==0 else answer