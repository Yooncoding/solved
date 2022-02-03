"""
11399 - ATM
https://www.acmicpc.net/problem/11399
"""

from sys import stdin

input = stdin.readline

n = int(input())
p = list(map(int, input().rsplit()))
p.sort()

for i in range(1, n):
    p[i] += p[i-1]

print(sum(p))
