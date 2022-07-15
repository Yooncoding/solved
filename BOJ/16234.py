"""
16234 - 치킨배달
https://www.acmicpc.net/problem/16234
"""

from collections import deque

# input
N, L, R = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]


def in_range(r, c):
    return 0 <= r < N and 0 <= c < N


def bfs(r, c):
    unit = []
    people = 0

    q = deque()
    q.append((r, c))
    unit.append((r, c))
    people += grid[r][c]
    visited[r][c] = True

    while len(q):
        r, c = q.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if in_range(nr, nc) and not visited[nr][nc]:
                if L <= abs(grid[nr][nc] - grid[r][c]) <= R:
                    q.append((nr, nc))
                    unit.append((nr, nc))
                    people += grid[nr][nc]
                    visited[nr][nc] = True

    newPeople = people // len(unit)

    for r, c in unit:
        grid[r][c] = newPeople

    return True if len(unit) >= 2 else False


ans = 0
while True:
    visited = [[False for _ in range(N)] for _ in range(N)]
    process = False
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                check = bfs(i, j)
                if check:
                    process = True

    if not process:
        break

    ans += 1

print(ans)
