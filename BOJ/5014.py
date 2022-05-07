"""
5014 - 스타트링크
https://www.acmicpc.net/problem/5014
"""

from sys import stdin
from collections import deque

input = stdin.readline

f, s, g, u, d = map(int, input().rsplit())
q = deque()
q.append([s, 0])
visited = [False for _ in range(f+1)]
visited[s] = True
while len(q):
    x, cnt = q.popleft()
    if x == g:
        print(cnt)
        break
    dx = [u, -d]
    for i in range(2):
        nx = x + dx[i]
        if 0 < nx <= f and not visited[nx]:
            q.append([nx, cnt+1])
            visited[nx] = True
else:
    print("use the stairs")
