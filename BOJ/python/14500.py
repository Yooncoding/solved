"""
14500 - 테트로미노
https://www.acmicpc.net/problem/14500
"""

from sys import stdin

input = stdin.readline

max_v = 0
paper = []
n, m = map(int, input().rsplit())
visited = [[False for _ in range(m)]for _ in range(n)]
for _ in range(n):
    paper.append(list(map(int, input().rsplit())))


def dfs(x, y, tsum, cnt):
    global max_v

    d = [(1, 0), (0, -1), (-1, 0), (0, 1)]

    if cnt == 4:
        max_v = max(max_v, tsum)
        return

    for i in range(4):
        nx = x + d[i][0]
        ny = y + d[i][1]

        if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx]:
            visited[ny][nx] = True
            dfs(nx, ny, tsum + paper[ny][nx], cnt + 1)
            visited[ny][nx] = False


def tdfs(x, y, tsum):
    global max_v

    d = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    for i in range(4):
        flag = False
        for j in range(4):
            if i == j:
                continue
            nx = x + d[j][0]
            ny = y + d[j][1]
            if 0 <= nx < m and 0 <= ny < n:
                tsum += paper[ny][nx]
            else:
                flag = True
                break
        if not flag:
            max_v = max(max_v, tsum)
        tsum = paper[y][x]


for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(j, i, paper[i][j], 1)
        visited[i][j] = False

        tdfs(j, i, paper[i][j])

print(max_v)
