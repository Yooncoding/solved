"""
1676 - 팩토리얼 0의 개수
https://www.acmicpc.net/problem/1676
"""

from sys import stdin

input = stdin.readline

N = int(input())
val = 1
cnt = 0

for i in range(1, N+1):
    val *= i

for j in str(val)[::-1]:
    if j != "0":
        break
    cnt += 1

print(cnt)
