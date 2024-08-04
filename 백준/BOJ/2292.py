"""
2292 - 벌집
https://www.acmicpc.net/problem/2292
"""

from sys import stdin

input = stdin.readline

n = int(input())
i, cnt = 1, 1
while True:
    if n <= i:
        print(cnt)
        break
    i += (6 * cnt)
    cnt += 1
