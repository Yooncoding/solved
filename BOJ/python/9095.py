"""
9095 - 1, 2, 3 더하기
https://www.acmicpc.net/problem/9095
"""

from sys import stdin

input = stdin.readline

dp = [0, 1, 2, 4] + [0] * 8
for i in range(4, 12):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for T in range(int(input())):
    n = int(input())
    print(dp[n])
