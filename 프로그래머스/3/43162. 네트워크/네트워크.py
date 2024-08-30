from collections import deque


def solution(n, computers):
    answer = 0    
    visited = [False for _ in range(n)]
    
    def bfs(start):
        q = deque()
        q.append(start)
        
        while len(q):
            v = q.popleft()
            visited[v] = True
            
            for nv in range(n):
                if not visited[nv] and computers[v][nv] == 1 and v != nv:
                    visited[nv] = True
                    q.append(nv)
    
    
    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1

    
    return answer