def solution(arr):
    answer = [0, 0]
    length = len(arr)
    def quadpress(r, c, l):
        start = arr[r][c]
            
        for i in range(r, r+l):
            for j in range(c, c+l):
                if start != arr[i][j]:
                    l //= 2
                    quadpress(r, c, l)
                    quadpress(r, c+l, l)
                    quadpress(r+l, c, l)
                    quadpress(r+l, c+l, l)
                    return
                
        answer[start] += 1
        
    
    quadpress(0, 0, length)
        
    return answer