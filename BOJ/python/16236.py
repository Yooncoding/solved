"""
16236 - 아기 상어
https://www.acmicpc.net/problem/16236
"""

from sys import stdin

input = stdin.readline

space = []
N = int(input())
for _ in range(N):
    space.append(list(map(int, input().rsplit())))


def go(y, x, size, temp_size, cnt):
    q = []
    q.append([0, [y, x]])
    visited = [[False for _ in range(N)] for _ in range(N)]
    dx, dy = [0, -1, 1, 0], [-1, 0, 0, 1]

    space[y][x] = 0

    if temp_size == size:
        temp_size = 0
        size += 1

    while len(q) != 0:
        q.sort(key=lambda x: (x[0], x[1][0], x[1][1]))
        n, point = q.pop(0)
        y, x = point

        if visited[y][x] is True:
            continue

        if space[y][x] < size and space[y][x] != 0:
            space[y][x] = 0
            temp_size += 1
            cnt += n
            return go(y, x, size, temp_size, cnt)

        for m in range(4):
            nx, ny = x + dx[m], y + dy[m]
            if 0 <= nx < N and 0 <= ny < N and space[ny][nx] <= size:
                q.append([n + 1, [ny, nx]])

        visited[y][x] = True

    return cnt


answer = 0

for i in range(N):
    for j in range(N):
        if space[j][i] == 9:
            y, x = j, i

answer = go(y, x, 2, 0, 0)  # y, x, size, temp_size, cnt

print(answer)
