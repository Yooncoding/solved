"""
9461 - 파도반 수열
https://www.acmicpc.net/problem/9461
"""

from sys import stdin

input = stdin.readline

dp = [1, 1, 1] + [0] * 97

for i in range(3, 100):
    dp[i] = dp[i-3] + dp[i-2]

for _ in range(int(input())):
    print(dp[int(input())-1])
