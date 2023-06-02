def solution(progresses, speeds):
    answer = []
    queue = [0] * len(progresses)
    last = 0
    cnt = 0
    tmp = 0
    
    for i in range(1, 101):
        
        for j in range(len(progresses)):

            if progresses[j] < 100:
            
                progresses[j] += speeds[j]

                if progresses[j] >= 100:
                    
                    queue[j] = 1
                    
        if queue[last] == 1 :

            print(last)
            
            for j in range(last, len(queue)): 
                if queue[j] == 0:
                    last = j
                    break
                if j == len(queue)-1:
                    tmp = 1
                cnt += 1
                
            if tmp == 1:
                last = len(progresses)
                           
            answer.append(cnt)
    
            cnt = 0

        if last == len(progresses):
            break
                    
                    
    return answer