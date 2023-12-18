def solution(stones, k):
    answer = 0
    left, right = 1, max(stones)
    
    while left <= right :
        check = 0
        mid = (left+right)//2
        for stone in stones:
            if (stone-mid) <= 0:
                check += 1
            else:
                check = 0
            if check == k:
                break
        # 좀 더 건너갈 수 있음(포문이 끝났는데도 최대치에 도달 못함)
        if check < k:
            left = mid + 1
        # 이게 숫자가 정답이거나 덜 건너가야 됨
        else:
            answer = mid
            right = mid - 1
    return answer
        