"""
6064 - 카잉달력
https://www.acmicpc.net/problem/6064
"""

from sys import stdin

input = stdin.readline

for _ in range(int(input())):
    m, n, x, y = map(int, input().split())
    while x <= m * n:
        if (x - y) % n == 0:
            print(x)
            break
        x += m
    else:
        print(-1)
