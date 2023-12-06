def LCD(a, b):
    A, B = a, b
    while B > 0:
        A, B = B, A%B
    
    return (a*b)//A

def solution(arr):
    answer = 1
    arr.sort(reverse = True)
    tmp = arr[0]
    for i in range(len(arr)-1):
        tmp = LCD(tmp, arr[i+1])
    
    answer = tmp
                
    return answer