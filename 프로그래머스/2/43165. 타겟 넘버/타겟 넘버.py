def solution(numbers, target):
    global answer
    answer = 0
    
    def dfs(cur, cnt):
        global answer
        if cnt == len(numbers):
            if cur == target:
                answer += 1
            return
        
        dfs(cur+numbers[cnt], cnt+1)
        dfs(cur-numbers[cnt], cnt+1)
        
    
    dfs(0, 0)

    return answer