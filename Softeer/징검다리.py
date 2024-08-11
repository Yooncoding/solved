"""
https://softeer.ai/practice/6293
24-08-12
"""

import sys

input = sys.stdin.readline

n = int(input())
heights = list(map(int, input().rsplit()))

dp = [0] * n
for i in range(n):
    for j in range(i):
        if heights[j] < heights[i]:
            dp[i] = max(dp[i], dp[j] + 1)
    dp[i] = max(dp[i], 1)

print(max(dp))