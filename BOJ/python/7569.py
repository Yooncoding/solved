"""
7569 - 토마토
https://www.acmicpc.net/problem/7569
"""

from sys import stdin
from collections import deque

input = stdin.readline

M, N, H = map(int, input().rsplit())
box = []

for _ in range(H):
    one = []
    for _ in range(N):
        one.append(list(map(int, input().rsplit())))
    box.append(one)

answer = 0
q = deque()

for k in range(H):
    for j in range(N):
        for i in range(M):
            if box[k][j][i] == 1:
                q.append([i, j, k])

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

while len(q) != 0:
    x, y, z = q.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]

        if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H:
            if box[nz][ny][nx] == 0:
                q.append([nx, ny, nz])
                box[nz][ny][nx] = box[z][y][x] + 1

for k in range(H):
    for j in range(N):
        answer = max(answer, max(box[k][j]))
        for i in range(M):
            if box[k][j][i] == 0:
                print(-1)
                exit(0)

print(answer - 1)