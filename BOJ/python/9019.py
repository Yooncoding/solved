"""
9019 - DSLR
https://www.acmicpc.net/problem/9019
"""

from sys import stdin
from collections import deque

input = stdin.readline


def bfs(start, dest):
    q = deque()
    q.append((start, ""))
    visited = [False for _ in range(10000)]
    while len(q):
        n, comm = q.popleft()
        t = str(n)
        t = (4 - len(t)) * "0" + t

        if n == dest:
            print(comm)
            return True

        d = 2 * n % 10000
        s = n - 1 if n != 0 else 9999
        left = int(t[1] + t[2] + t[3] + t[0])
        right = int(t[3] + t[0] + t[1] + t[2])

        if not visited[d]:
            q.append((d, comm + "D"))
            visited[d] = True

        if not visited[s]:
            q.append((s, comm + "S"))
            visited[s] = True

        if not visited[left]:
            q.append((left, comm + "L"))
            visited[left] = True

        if not visited[right]:
            q.append((right, comm + "R"))
            visited[right] = True

    return False


for T in range(int(input())):
    a, b = map(int, input().rsplit())
    bfs(a, b)
