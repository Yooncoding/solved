"""
15685 - 드래곤 커브
https://www.acmicpc.net/problem/15685
"""

# input
n = int(input())


def in_range(y, x):
    return 0 <= y <= 100 and 0 <= x <= 100


def go(x, y, d, g):
    past_dir_nums = [d]
    nx, ny = x + dx[d], y + dy[d]
    visited[ny][nx] = True
    x, y = nx, ny

    while g > 0:
        for past_dir_num in list(reversed(past_dir_nums)):
            dir_num = (past_dir_num + 1) % 4
            past_dir_nums.append(dir_num)
            nx, ny = x + dx[dir_num], y + dy[dir_num]
            if in_range(ny, nx):
                visited[ny][nx] = True
            x, y = nx, ny

        g -= 1

    return


dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
visited = [[False for _ in range(101)] for _ in range(101)]
for _ in range(n):
    x, y, d, g = map(int, input().split())
    visited[y][x] = True
    go(x, y, d, g)

ans = 0
for i in range(100):
    for j in range(100):
        if visited[i][j] and visited[i][j+1] \
                and visited[i+1][j] and visited[i+1][j+1]:
            ans += 1

print(ans)
