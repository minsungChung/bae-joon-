def solution(n, words):
    answer = []
    dict = {words[0][0]:[words[0]]}
    turn = 2
    pre = words[0][-1]
    cnt = 1
    for i in range(1, len(words)):
        if turn == n+1:
            turn = 1
            cnt += 1
        if words[i][0] != pre:
            answer = [turn, cnt]
            break
        if words[i][0] not in dict.keys():
            dict[words[i][0]] = [words[i]]
        else:
            if words[i] in dict[words[i][0]]:
                answer = [turn, cnt]
                break
            else:
                dict[words[i][0]].append(words[i])
        pre = words[i][-1]
        turn += 1
                
    if len(answer) == 0:
        answer = [0, 0]

    return answer