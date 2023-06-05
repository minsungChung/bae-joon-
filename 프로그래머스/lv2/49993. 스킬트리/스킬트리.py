def solution(skill, skill_trees):
    answer = 0
    
    for skills in skill_trees:
        stack = []
        tmp = 0
        for s in skills:
            if s in skill:
                stack.append(s)
                if stack[len(stack)-1] != skill[len(stack)-1]:
                    tmp = 1
                    break
        
        if tmp == 0:
            answer += 1
    return answer