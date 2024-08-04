"""
15650 - N과 M(2)
https://www.acmicpc.net/problem/15650
"""

from sys import stdin

input = stdin.readline

def dfs(L, s):
    if L == m:
        print(*res)
    else:
        for i in range(s, n + 1):
            res[L] = i
            dfs(L + 1, i + 1)


n, m = map(int, input().split())
res = [0] * m
dfs(0, 1)
