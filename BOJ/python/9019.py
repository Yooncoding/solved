"""
9019 - DSLR
https://www.acmicpc.net/problem/9019
"""

from sys import stdin
from collections import deque

input = stdin.readline


def cmd_D(n):
    d = n * 2
    if d > 9999:
        d %= 10000
    return d


def cmd_S(n):
    s = n - 1
    if n == 0:
        s = 9999
    return s


def cmd_L(n):
    l = ((n % 1000) * 10) + n // 1000
    return l


def cmd_R(n):
    r = ((n % 10) * 1000) + n // 10
    return r


def bfs(ori, dest):
    Q = deque()
    Q.append(["", ori])
    visited = [False for _ in range(10000)]
    while len(Q) != 0:
        cmds, n = Q.popleft()
        if n == dest:
            break

        D = cmd_D(n)
        if visited[D] == False:
            visited[D] = True
            Q.append([cmds + "D", D])

        S = cmd_S(n)
        if visited[S] == False:
            visited[S] = True
            Q.append([cmds + "S", S])

        L = cmd_L(n)
        if visited[L] == False:
            visited[L] = True
            Q.append([cmds + "L", L])

        R = cmd_R(n)
        if visited[R] == False:
            visited[R] = True
            Q.append([cmds + "R", R])

    return cmds


for _ in range(int(input())):
    A, B = map(int, input().rsplit())
    print(bfs(A, B))
