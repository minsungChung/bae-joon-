def solution(numbers):
    answer = ''
    nums = []
    for n in numbers:
        nts = str(n)
        tmp = [nts*(6//len(nts)), len(nts)]
        nums.append(tmp)
    
    nums.sort(reverse=True)
    if nums[0][0][0] == '0':
        return '0'
        
    for num in nums:
        answer += num[0][:num[1]]
    
    
    return answer