def solution(user_id, banned_id):
    l = len(banned_id)
    banned_pos = [[] for _ in range(l)]
    for i in range(l):
        for j in range(len(banned_id[i])):
            if banned_id[i][j] == '*':
                banned_pos[i].append(j)
                
    cans = []            
    for i in range(l):
        can = []
        for j in range(len(user_id)):
            tmp = list(user_id[j])
            if len(tmp) == len(banned_id[i]):
                for k in banned_pos[i]:
                    tmp[k] = '*'
                word = ''.join(tmp)

                if word == banned_id[i]:
                    can.append(user_id[j])
        cans.append(can)
    p = []
    def dfs(pair, n, start):
        if len(pair) == n and set(pair) not in p:
            p.append(set(pair))
            return
        if start >= n:
            return
        
        for i in range(start, n):
            for j in range(len(cans[i])):
                if cans[i][j] not in pair:
                    pair.append(cans[i][j])
                    dfs(pair, n, i+1)
                    pair.pop()
    
    dfs([], l, 0)
            
    return len(p)