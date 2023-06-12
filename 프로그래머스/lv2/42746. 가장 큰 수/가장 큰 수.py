def solution(numbers):
    answer = ''
    numbers = [str(n) for n in numbers]
    numbers.sort(key=lambda x : (x*4)[:4], reverse=True)
    
    # 0만 있을 때
    if numbers[0] == '0':
        answer = '0'
    else:
        answer = ''.join(numbers)
    return answer