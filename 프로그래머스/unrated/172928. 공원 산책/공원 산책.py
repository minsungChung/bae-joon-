def solution(park, routes):
    answer = []
    width = len(park[0])
    start = [0, 0]
    is_bothered = False
    
    for i in range(len(park)):
        for j in range(width):
            if park[i][j] == 'S':
                start[0] = i
                start[1] = j
                break
    
    current = start[:]
    
    for order in routes:
        # 현재 위치 복사
        tmp = current[:]
        check = 0
        
        direction, num = order.split()
        if direction == 'N':
            tmp[0] -= int(num)
            
            if tmp[0] >= 0 :
                for i in range(tmp[0], current[0]+1):
                    if park[i][current[1]] == 'X':
                        check = 1
                        break
                        
                if check == 0:
                    current[0] = tmp[0]
                
        elif direction == 'S':
            tmp[0] += int(num)
            
            if tmp[0] < len(park) :
                for i in range(current[0], tmp[0]+1):
                    if park[i][current[1]] == 'X':
                        check = 1
                        break
                        
                if check == 0:
                    current[0] = tmp[0]
            
        elif direction == 'W':
            tmp[1] -= int(num)
            
            if tmp[1] >= 0 :
                for i in range(tmp[1], current[1]+1):
                    if park[current[0]][i] == 'X':
                        check = 1
                        break
                        
                if check == 0:
                    current[1] = tmp[1]
            
        elif direction == 'E':
            tmp[1] += int(num)
            
            if tmp[1] < width :
                for i in range(current[1], tmp[1]+1):
                    if park[current[0]][i] == 'X':
                        check = 1
                        break
                        
                if check == 0:
                    current[1] = tmp[1]
    answer = current
    return answer