def solution(word):
    global seq
    result = {}
    seq = 0
    
    def dfs(cur, cnt):
        global seq
        
        if cnt > 5:
            return
        
        result[cur] = seq
        seq += 1
        
        for c in "AEIOU":
            dfs(cur+c, cnt+1)
    
        return
    
    
    dfs("", 0)
    answer = result[word]
        
    return answer