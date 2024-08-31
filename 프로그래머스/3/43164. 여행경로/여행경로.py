def solution(tickets):
    answer = []
    n = len(tickets)
    tickets.sort(key = lambda x : x[1])
    
    def dfs(cur_idx, cnt):
        # 이미 모든 항공권을 탐색했을 때, answer에 결과가 들어있음 
        # 추가 탐색 방지로 분기 처리
        if len(answer):
            return
        
        if cnt == n:
            answer.append("ICN")
            for i in path:
                answer.append(tickets[i][1])
            
            return
        

        for next_idx in range(n):
            if tickets[cur_idx][1] == tickets[next_idx][0] and not used[next_idx]:
                used[next_idx] = True
                path.append(next_idx)
                dfs(next_idx, cnt+1)
                used[next_idx] = False
                path.pop()
        
        return
            
        
    for i in range(n):
        used = [False for _ in range(n)]
        if tickets[i][0] == "ICN" and not len(answer):
            path = [i]
            used[i] = True
            dfs(i, 1)
        
        
    
    return answer