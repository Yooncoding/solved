"""
2667 - 단지번호붙이기
https://www.acmicpc.net/problem/2667
"""

from sys import stdin
from collections import deque

input = stdin.readline

N = int(input())
apartment = []
visited = [[False for _ in range(N)] for _ in range(N)]
result = []


def bfs(x, y):
    q = deque()
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    q.append([x, y])
    cnt = 0
    while len(q) != 0:
        x, y = q.popleft()
        if visited[x][y] == True:
            continue
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and apartment[nx][ny] == 1:
                q.append([nx, ny])
        visited[x][y] = True
        cnt += 1

    return cnt


for i in range(N):
    apartment.append(list(map(int, input().rstrip())))

for b in range(N):
    for a in range(N):
        if visited[a][b] == True:
            continue
        if apartment[a][b] == 1:
            result.append(bfs(a, b))

result.sort()

print(len(result))
for answer in result:
    print(answer)
