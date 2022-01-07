"""
7576 - 토마토
https://www.acmicpc.net/problem/7576
"""

from sys import stdin
from collections import deque

input = stdin.readline

M, N = map(int, input().rsplit())
box = []
for i in range(N):
    box.append(list(map(int, input().rsplit())))

answer = 0

q = deque()
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for i in range(M):
    for j in range(N):
        if box[j][i] == 1:
            q.append([i, j])

while len(q) != 0:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and box[ny][nx] == 0:
            box[ny][nx] = box[y][x] + 1
            q.append([nx, ny])

for i in range(M):
    for j in range(N):
        if box[j][i] == 0:
            answer = 0
            break
        answer = max(answer, box[j][i])
    if answer == 0:
        break

print(answer - 1)
