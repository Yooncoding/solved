"""
9461 - 파도반 수열
https://www.acmicpc.net/problem/9461
"""

from sys import stdin

input = stdin.readline

dp = [1, 1, 1, 2, 2] + [0] * 95

for i in range(5, 100):
    dp[i] = dp[i - 1] + dp[i - 5]

for T in range(int(input())):
    n = int(input())
    print(dp[n - 1])
