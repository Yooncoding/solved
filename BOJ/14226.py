"""
14226 - 이모티콘
https://www.acmicpc.net/problem/14226
"""

from sys import stdin
from collections import deque

input = stdin.readline

s = int(input())
visited = [[False for _ in range(2001)] for _ in range(2001)]
q = deque()
q.append((1, 0, 0))
while len(q):
    screen, clipboard, time = q.popleft()
    if screen == s:
        ans = time
        break

    if screen > 2000 or clipboard > 2000 or visited[screen][clipboard]:
        continue

    visited[screen][clipboard] = True

    if screen > 0:
        q.append((screen, screen, time+1))
        q.append((screen-1, clipboard, time+1))
    if clipboard > 0:
        q.append((screen+clipboard, clipboard, time+1))

print(ans)
