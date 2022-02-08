"""
17626 - Four Squares
https://www.acmicpc.net/problem/17626
"""

from sys import stdin

input = stdin.readline

n = int(input())

dp = [0 for _ in range(50001)]
dp[1] = 1

for i in range(2, n+1):
    j = 1
    cnt = 4
    while j**2 <= i:
        cnt = min(cnt, dp[i - j**2])
        j += 1
    dp[i] = cnt + 1

print(dp[n])
