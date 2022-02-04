"""
9375 - 패션왕 신해빈
https://www.acmicpc.net/problem/9375
"""

from sys import stdin
from collections import defaultdict

input = stdin.readline


for _ in range(int(input())):
    n = int(input())
    clothes = defaultdict(int)
    cnt = 1
    for _ in range(n):
        name, kind = input().rsplit()
        clothes[kind] += 1
    for kind in clothes:
        cnt *= (clothes[kind] + 1)
    print(cnt - 1)
