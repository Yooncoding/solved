"""
2178 - 미로 탐색
https://www.acmicpc.net/problem/2178
"""

from sys import stdin
from collections import deque

input = stdin.readline

N, M = map(int, input().rsplit())
miro = []

for _ in range(N):
    miro.append(list(map(int, input().rstrip())))


def go():
    q = deque()
    q.append([1, [0, 0]])
    visited = [[False for _ in range(M)] for _ in range(N)]

    while len(q) != 0:
        cnt, point = q.popleft()
        x, y = point
        dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

        if visited[x][y] == True:
            continue

        if x == N - 1 and y == M - 1:
            break

        for m in range(4):
            nx, ny = x + dx[m], y + dy[m]

            if 0 <= nx < N and 0 <= ny < M and miro[nx][ny] == 1:
                if visited[nx][ny] == False:
                    q.append([cnt + 1, [nx, ny]])

        visited[x][y] = True
    return cnt


print(go())
