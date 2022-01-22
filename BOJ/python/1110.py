"""
1110 - 더하기 사이클
https://www.acmicpc.net/problem/1110
"""

from sys import stdin

input = stdin.readline

n = int(input())
cnt = 0

if n // 10 == 0:
    n *= 10

dest = n

while cnt == 0 or dest != n:
    a = n // 10
    b = n % 10
    t = a + b
    n = b * 10 + (t % 10)
    cnt += 1

print(cnt)
