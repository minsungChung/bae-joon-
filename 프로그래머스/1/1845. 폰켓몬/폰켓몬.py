from collections import defaultdict

def solution(nums):
    answer = len(nums)//2
    
    d = defaultdict(int)
    
    for n in nums:
        d[n] += 1
        
    kinds = len(d.keys())
        
    if answer > kinds:
        answer = kinds
    
    return answer