def solution(triangle):
    answer = 0
    n = len(triangle)
    dp = [0 for _ in range((n*(n+1))//2)]
    dp[0] = triangle[0][0]
    
    for i in range(1, n):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[(i*(i+1))//2+j] = dp[(i*(i+1))//2+j-i] + triangle[i][j]
            elif j == len(triangle[i])-1:
                dp[(i*(i+1))//2+j] = dp[(i*(i+1))//2+j-i-1] + triangle[i][j]
            else:
                m = max(dp[(i*(i+1))//2+j-i], dp[(i*(i+1))//2+j-i-1])
                dp[(i*(i+1))//2+j] = m + triangle[i][j]
                
    answer = max(dp[-len(triangle[n-1]):])

            
    return answer