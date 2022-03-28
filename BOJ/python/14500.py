"""
14500 - 테트로미노
https://www.acmicpc.net/problem/14500
"""

from sys import stdin
from itertools import combinations

input = stdin.readline

n, m = map(int, input().rsplit())
ground = []
for _ in range(n):
    ground.append(list(map(int, input().rsplit())))

dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]
visited = [[False for _ in range(m)] for _ in range(n)]

max_v = max(map(max, ground))
ans = 0


def dfs(y, x, cnt, tsum):
    global ans
    # global max_v

    if ans >= tsum + (4-cnt) * max_v:
        return

    if cnt == 4:
        # ans가 함수안에서 변경되기 때문에 global 필요, max_v는 global 불필요
        ans = max(ans, tsum)
        return

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
            visited[ny][nx] = True
            dfs(ny, nx, cnt+1, tsum+ground[ny][nx])
            visited[ny][nx] = False

    return


def bfs(y, x):
    global ans

    for combi in combinations(range(4), 3):
        tsum = ground[y][x]
        for i in combi:
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                tsum += ground[ny][nx]
        ans = max(ans, tsum)

    return


for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, ground[i][j])
        visited[i][j] = False

        bfs(i, j)

print(ans)
