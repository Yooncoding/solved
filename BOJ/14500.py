"""
14500 - 테트로미노
https://www.acmicpc.net/problem/14500
"""

# input
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]  # 상 하 좌 우
visited = [[False for _ in range(m)] for _ in range(n)]


def in_range(r, c):
    return 0 <= r < n and 0 <= c < m


def dfs(r, c, s, cnt):
    global ans
    # 가지치기
    # 행렬에서 가장 큰 수 * 남은 횟수 + 현재 까지 합이 현재까지의 최대값보다 작으면 이후 시행할 필요 없음
    if max_value_in_grid * (4-cnt) + s <= ans:
        return

    if cnt == 4:
        ans = max(s, ans)
        return

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if in_range(nr, nc) and not visited[nr][nc]:
            if cnt == 2:
                visited[nr][nc] = True
                dfs(r, c, s + grid[nr][nc], cnt + 1)
                visited[nr][nc] = False

            visited[nr][nc] = True
            dfs(nr, nc, s + grid[nr][nc], cnt+1)
            visited[nr][nc] = False

    return


ans = 0
max_value_in_grid = max(map(max, grid))  # 행렬에서 가장 큰 수
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, grid[i][j], 1)
        visited[i][j] = False

print(ans)
