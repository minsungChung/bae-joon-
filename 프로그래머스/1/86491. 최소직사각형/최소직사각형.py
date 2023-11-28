def solution(sizes):
    answer = 0
    max_width = 0
    max_height = 0
    
    for card in sizes:
        if card[0] < card[1]:
            tmp = card[0]
            card[0] = card[1]
            card[1] = tmp
            
        max_width = max(max_width, card[0])
        max_height = max(max_height, card[1])
            
    return max_width * max_height