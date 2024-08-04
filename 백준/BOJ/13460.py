"""
13460 - 구슬 탈출 2
https://www.acmicpc.net/problem/13460
"""

from collections import deque

n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]

compass = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우


def move(r, c, direction):
    dr, dc = direction
    move_cnt = 0
    while True:
        nr, nc = r + dr, c + dc
        if grid[nr][nc] == '#' or grid[r][c] == 'O':
            break
        r, c = nr, nc
        move_cnt += 1

    return r, c, move_cnt


def bfs(red, blue):
    q = deque()
    q.append([red, blue, 0])
    visited = []
    visited.append([red, blue])
    while len(q):
        red, blue, cnt = q.popleft()
        rr, rc = red
        br, bc = blue
        if cnt == 10:
            continue

        for i in range(4):
            nrr, nrc, red_move_cnt = move(rr, rc, compass[i])
            nbr, nbc, blue_move_cnt = move(br, bc, compass[i])

            if grid[nbr][nbc] == 'O':
                continue

            if grid[nrr][nrc] == 'O':
                return cnt + 1

            if nrr == nbr and nrc == nbc:
                if red_move_cnt > blue_move_cnt:
                    nrr -= compass[i][0]
                    nrc -= compass[i][1]
                else:
                    nbr -= compass[i][0]
                    nbc -= compass[i][1]

            nred, nblue = (nrr, nrc), (nbr, nbc)
            if [nred, nblue] not in visited:
                visited.append([nred, nblue])
                q.append([nred, nblue, cnt + 1])

    return -1


for i in range(n):
    for j in range(m):
        if grid[i][j] == 'R':
            red_marble = (i, j)
        if grid[i][j] == 'B':
            blue_marble = (i, j)

ans = bfs(red_marble, blue_marble)
print(ans)
