from sys import stdin
from collections import deque

input = stdin.readline

def in_range(r, c):
  return 0 <= r < n and 0 <= c < m

def can_go(r, c):
  return graph[r][c] != 'X' and not visited[r][c]
  

dr, dc = [0, -1, 0, 1], [1, 0, -1, 0]

def start(r, c):
  cnt = 0
  q = deque()
  q.append([r, c])
  while len(q):
    r, c = q.popleft()
    for i in range(4):
      nr, nc = r + dr[i], c + dc[i]
      if in_range(nr, nc) and can_go(nr, nc):
        if graph[nr][nc] == 'P':
          cnt += 1
        visited[nr][nc] = True
        q.append([nr, nc])
        
  return cnt if cnt != 0 else 'TT'
  

n, m = map(int, input().rsplit())
graph = [list(input().rstrip()) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

for i in range(n):
  for j in range(m):
    if graph[i][j] == 'I':
      visited[i][j] = True
      answer = start(i, j)

print(answer)
  