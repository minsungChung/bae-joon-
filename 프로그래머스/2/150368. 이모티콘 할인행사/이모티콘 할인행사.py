def solution(users, emoticons):
    answer = [0, 0]
    discount_rates = [0.9, 0.8, 0.7, 0.6]
    pairs = []
    l = len(emoticons)
    def dfs(n, pair):
        if len(pair) == n:
            pairs.append(pair[:])
            return
        
        for d in discount_rates:
            pair.append(d)
            dfs(n, pair)
            pair.pop()
                
    dfs(l, [])
    
    for pair in pairs:
        tmp = [0, 0]
        for user in users:
            total = 0
            for i in range(l):
                if user[0] <= 100-(pair[i]*100):
                    total += emoticons[i]*pair[i]
            if user[1] <= total:
                tmp[0] += 1
            else:
                tmp[1] += total
        if tmp[0] > answer[0] or (tmp[0] == answer[0] and tmp[1] > answer[1]):
            answer = tmp

    return answer