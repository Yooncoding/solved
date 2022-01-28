"""
1697 - 숨바꼭질
https://www.acmicpc.net/problem/1697
"""

from sys import stdin
from collections import deque

input = stdin.readline

N, M = map(int, input().rsplit())

visited = [False] * 100000 + [False]
q = deque()
q.append([0, N])

while len(q) != 0:
    cnt, x = q.popleft()
    if x > 100000 or x < 0:
        continue
    if visited[x] is True:
        continue
    if x == M:
        break

    q.append([cnt + 1, x - 1])
    q.append([cnt + 1, x + 1])
    q.append([cnt + 1, x * 2])

    visited[x] = True
print(cnt)
