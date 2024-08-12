def solution(targets):
    targets.sort(key=lambda x:(x[1],x[0]))
    answer = 0
    
    flag = -1
    for target in targets:
        if flag <= target[0]:
            flag = target[1]
            answer += 1
    
    
    return answer