from collections import deque


def solution(maps):
    answer = 0
    
    dr, dc = [0, -1, 0, 1], [1, 0, -1, 0]
    n, m  = len(maps), len(maps[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    def in_range(r, c):
        return 0 <= r < n and 0 <= c < m
    
    def can_go(r, c):
        return not visited[r][c] and maps[r][c] == 1
    
    def bfs(start):
        q = deque()
        q.append([start, 1])
        visited[start[0]][start[1]] = True
        
        while len(q):
            [r, c], cnt = q.popleft()
            
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if in_range(nr, nc) and can_go(nr, nc):
                    if nr == n-1 and nc == m-1:
                        return cnt+1
                    q.append([[nr, nc], cnt+1])
                    visited[nr][nc] = True
            
        return -1
        
        
    answer = bfs([0, 0])

    return answer