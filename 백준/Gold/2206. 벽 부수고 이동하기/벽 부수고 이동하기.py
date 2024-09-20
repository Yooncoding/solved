from sys import stdin
from collections import deque

input = stdin.readline

n, m = map(int, input().rsplit())
ground = [list(map(int, input().rstrip())) for _ in range(n)]

dr, dc = [0, -1, 0, 1], [1, 0, -1, 0]
visited = [[[0 for _ in range(2)] for _ in range(m)] for _ in range(n)]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < m


def bfs():
    q = deque()
    q.append([0, 0, 0])
    visited[0][0][0] = 1

    while len(q):
        r, c, u = q.popleft()
        if r == n - 1 and c == m - 1:
            return visited[r][c][u]

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if in_range(nr, nc):
                if ground[nr][nc] == 0 and visited[nr][nc][u] == 0:
                    visited[nr][nc][u] = visited[r][c][u] + 1
                    q.append([nr, nc, u])

                elif ground[nr][nc] == 1 and u == 0:
                    visited[nr][nc][u+1] = visited[r][c][u] + 1
                    q.append([nr, nc, u+1])

    return -1


print(bfs())