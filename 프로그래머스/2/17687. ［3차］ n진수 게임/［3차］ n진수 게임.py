# n진법, 미리 구할 숫자 t, 참가인원 m, 순서 p
def solution(n, t, m, p):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    answer = ''
    i = 0
    start = 0
    num = "0"
    while True:
        if len(num) >= m*t:
            break
        i += 1
        tmp = i
        nn = ""
        while tmp >= n:
            nn += numbers[tmp%n]
            tmp //= n
        num += numbers[tmp]
        num += nn[::-1]

    for j in range(p-1, len(num), m):
        answer += num[j]
        if len(answer) >= t:
            break
        
        
    return answer