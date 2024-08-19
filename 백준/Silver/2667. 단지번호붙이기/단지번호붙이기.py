from sys import stdin
from collections import deque

input = stdin.readline

n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
dr, dc = [0, -1, 0, 1], [-1, 0, 1, 0]

def bfs(start_r, start_c):
  q = deque()
  q.append([start_r, start_c])
  cnt = 1
  visited[start_r][start_c] = True
  while len(q):
    r, c = q.popleft()
    for i in range(4):
      nr, nc = dr[i] + r, dc[i] + c
      if 0 <= nr < n and 0 <= nc < n:
        if graph[nr][nc] == 1 and not visited[nr][nc]:
          cnt += 1
          visited[nr][nc] = True
          q.append([nr, nc])
      
  return cnt

ans = []
for i in range(n):
  for j in range(n):
    if graph[i][j] == 1 and not visited[i][j]:
      result = bfs(i, j)
      ans.append(result)
      
ans.sort()
print(len(ans))
for k in ans:
  print(k)