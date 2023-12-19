def solution(gems):
    N = len(gems)
    answer = [0, N-1]
    # 전체 보석 종류
    kind = len(set(gems))
    # 종류 체크할 딕셔너리
    dic = {gems[0]:1,}
    # 투포인터
    s, e = 0, 0
    # start index와 end index가 모두 N안에 있을 때
    while s<N and e<N:
        # 보석 종류가 모자라면 end index를 하나 늘림
        if len(dic) < kind:
            e += 1
            if e == N:
                break
            # end index에 해당하는 dic에 보석이 있으면 +1 없으면 0
            dic[gems[e]] = dic.get(gems[e], 0) + 1
        # 보석 종류가 다 채워지면
        else:
            # 현재 정답에 저장된 길이보다 짧으면
            if (e-s+1) < (answer[1]-answer[0]+1):
                answer = [s, e]
            # 만약 맨 앞에 빼야되는 보석이 한개 있으면 dic에서 삭제
            if dic[gems[s]] == 1:
                del dic[gems[s]]
            # 아니면 개수만 하나 빼줌
            else:
                dic[gems[s]] -= 1
            # start index를 하나 늘림
            s += 1
            
    answer[0] += 1
    answer[1] += 1
            
    return answer