"""
1074 - Z
https://www.acmicpc.net/problem/1074
"""

from sys import stdin

input = stdin.readline

n, r, c = map(int, input().rsplit())
cnt = 0


def search(y, x, n):
    global cnt
    if y == r and x == c:
        print(cnt)
        return
    if not (y <= r < y + n and x <= c < x + n):
        cnt += n * n
        return
    if n == 1:
        cnt += 1
        return

    search(y, x, n//2)
    search(y, x+n//2, n//2)
    search(y+n//2, x, n//2)
    search(y+n//2, x+n//2, n//2)


search(0, 0, 2**n)
