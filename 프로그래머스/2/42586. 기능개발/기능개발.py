def solution(progresses, speeds):
    answer = []
    days = []
    cnt = 1
    
    l = len(progresses)
    
    # 나머지가 있으면 완료까지 + 1
    for i in range(l):
        day = (100-progresses[i]) // speeds[i]
        rest = (100-progresses[i]) % speeds[i]
        
        if rest > 0:
            day += 1
            
        days.append(day)
    
    # 제일 앞 기준
    base = days[0]
        
    for i in range(1, l):
        # 기준보다 큰 날짜가 나오면 그 날짜가 기준이 되고 그 전까지의 작업들 배포
        if days[i] > base:
            answer.append(cnt)
            base = days[i]
            cnt = 1
        else:
            cnt += 1
    answer.append(cnt)
            
    return answer