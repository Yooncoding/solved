"""
1003 - 피보나치 함수
https://www.acmicpc.net/problem/1003
"""

dp = [(1, 0), (0, 1)] + [0 for _ in range(39)]
for i in range(2, 41):
    dp[i] = (dp[i - 2][0] + dp[i - 1][0], dp[i - 2][1] + dp[i - 1][1])

for _ in range(int(input())):
    n = int(input())
    print(*dp[n])
