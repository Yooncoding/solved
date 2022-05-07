"""
16928 - 뱀과 사다리 게임
https://www.acmicpc.net/problem/16928
"""

from sys import stdin
from collections import deque

input = stdin.readline


n, m = map(int, input().rsplit())
board = [0 for _ in range(101)]
visited = [False for _ in range(101)]

for _ in range(n + m):
    x, y = map(int, input().rsplit())
    board[x] = y


def go():
    q = deque()
    dx = [1, 2, 3, 4, 5, 6]
    q.append([0, 1])
    while len(q) != 0:
        cnt, x = q.popleft()
        if x == 100:
            break
        for i in range(6):
            nx = x + dx[i]
            if nx > 100 or visited[nx] is True:
                continue
            if board[nx] != 0:
                q.append([cnt+1, board[nx]])
                visited[board[nx]] = True
            else:
                q.append([cnt+1, nx])
                visited[nx] = True
    return cnt


print(go())
