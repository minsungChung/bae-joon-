def solution(number, k):
    answer = ''
    # 모아 붙일 숫자
    collected = []
    
    for i, num in enumerate(number):
        # 모은 마지막 숫자보다 크고 아직 빼내야할 숫자가 남았을 때
        while len(collected) > 0 and collected[-1] < num and k > 0:
            collected.pop() # 마지막 숫자 빼기
            k -= 1 
        
        # 다 빼냈으면 collected에 넣기
        if k == 0:
            collected += list(number[i:])
            break
        
        # 새롭게 시작
        collected.append(num)
    
    # 빼내야하는 숫자가 남았을 수도 있으면 그냥 뒤를 삭제함
    collected = collected[:-k] if k > 0 else collected
    answer = ''.join(collected)
    return answer