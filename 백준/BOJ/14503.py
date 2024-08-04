"""
14503 - 로봇청소기
https://www.acmicpc.net/problem/14503
"""

from collections import deque

# input
n, m = map(int, input().split())
r, c, dir_num = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]


def bfs(r, c):
    global dir_num
    cnt = 1
    q = deque()
    q.append([r, c])
    grid[r][c] = 2
    while len(q):
        r, c = q.popleft()
        for _ in range(4):
            dir_num = (dir_num + 3) % 4
            nr, nc = r + dr[dir_num], c + dc[dir_num]
            if grid[nr][nc] == 0:
                q.append([nr, nc])
                grid[nr][nc] = 2
                cnt += 1
                break
        else:
            temp_dir_num = (dir_num + 2) % 4
            nr, nc = r + dr[temp_dir_num], c + dc[temp_dir_num]
            if grid[nr][nc] == 1:
                return cnt

            else:
                if grid[nr][nc] == 0:
                    q.append([nr, nc])
                    grid[nr][nc] = 2
                    cnt += 1
                else:
                    q.append([nr, nc])

    return cnt


ans = bfs(r, c)
print(ans)
