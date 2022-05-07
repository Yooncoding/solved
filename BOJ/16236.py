"""
16236 - 아기 상어
https://www.acmicpc.net/problem/16236
"""

from sys import stdin

input = stdin.readline

n = int(input())
area = []
for _ in range(n):
    area.append(list(map(int, input().rsplit())))

dy, dx = [-1, 0, 0, 1], [0, -1, 1, 0]


def bfs(y, x, size, ans, cnt):
    q = [((y, x), 0)]
    visited = [[False for _ in range(n)] for _ in range(n)]
    area[y][x] = 0

    while len(q):
        q.sort(key=lambda x: (x[1], x[0][0], x[0][1]))
        (y, x), d = q.pop(0)
        if visited[y][x]:
            continue
        if area[y][x] != 0 and area[y][x] < size:
            area[y][x] = 0
            ans += d
            cnt += 1
            if cnt == size:
                cnt = 0
                size += 1
                # 먹은 위치에서 너비 우선 탐색 재시작
            return bfs(y, x, size, ans, cnt)

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < n and area[ny][nx] <= size:
                q.append(((ny, nx), d + 1))

        visited[y][x] = True
    return ans


for i in range(n):
    for j in range(n):
        if area[i][j] == 9:
            y, x = i, j
ans = bfs(y, x, 2, 0, 0)
print(ans)
