"""
2579 - 계단 오르기
https://www.acmicpc.net/problem/2579
"""

from sys import stdin

input = stdin.readline

stair = [0]
n = int(input())
for _ in range(n):
    stair.append(int(input()))

if n == 1:
    print(stair[1])
else:
    dp = [0] * (n + 1)
    dp[1] = stair[1]
    dp[2] = stair[1] + stair[2]

    for i in range(3, n+1):
        dp[i] = max(dp[i-2] + stair[i], dp[i-3] + stair[i-1] + stair[i])

    print(dp[-1])
