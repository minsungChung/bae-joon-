def solution(numbers, hand):
    answer = ''
    pos_l = [3, 0]
    pos_r = [3, 2]
    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            pos_l = [num//3, 0]
        elif num in [3, 6, 9]:
            answer += 'R'
            pos_r = [num//3-1, 2]
        else:
            line = [3, 1]
            if num != 0:
                line = [num//3, 1]
            if abs(line[0] - pos_l[0]) + abs(line[1] - pos_l[1]) < abs(line[0] - pos_r[0]) + abs(line[1] - pos_r[1]):
                answer += 'L'
                pos_l = line
            elif abs(line[0] - pos_r[0]) + abs(line[1] - pos_r[1]) < abs(line[0] - pos_l[0]) + abs(line[1] - pos_l[1]):
                answer += 'R'
                pos_r = line
            else:
                if hand == "left":
                    answer += 'L'
                    pos_l = line
                else:
                    answer += 'R'
                    pos_r = line

    return answer