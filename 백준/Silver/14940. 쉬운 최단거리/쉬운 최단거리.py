from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]


def bfs(i, j):
  q = deque()
  q.append([i, j, 0])
  visited[i][j] = True
  while len(q):
    r, c, cnt = q.popleft()
    for i in range(4):
      nr, nc = r + dr[i], c + dc[i]
      if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
        if graph[nr][nc] == 0:
          continue
        else:
          ans[nr][nc] = cnt + 1
          visited[nr][nc] = True
          q.append([nr, nc, cnt + 1])

  return


ans = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
  for j in range(m): 
    if graph[i][j] == 2:
      bfs(i, j)

for i in range(n):
  for j in range(m):
    if not visited[i][j] and graph[i][j] == 1:
      ans[i][j] = -1

for row in ans:
    print(' '.join(map(str, row)))
