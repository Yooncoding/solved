"""
2178 - 미로 탐색
https://www.acmicpc.net/problem/2178
"""

from collections import deque

n, m = map(int, input().rsplit())
miro = []
for _ in range(n):
    miro.append(list(map(int, input().rstrip())))


def go():
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[0][0] = True
    q = deque()
    q.append([(0, 0), 1])
    while len(q):
        point, cnt = q.popleft()
        y, x = point
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
                if miro[ny][nx] == 0:
                    continue
                if ny == n - 1 and nx == m - 1:
                    print(cnt + 1)
                    return True

                q.append([(ny, nx), cnt + 1])
                visited[ny][nx] = True

    return False


go()
