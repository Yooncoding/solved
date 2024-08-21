"""
"""

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
max_value = 1000000

dp = [[max_value for _ in range(3)] for _ in range(n)]
dp[0][0] = cost[0][0]
dp[0][1] = cost[0][1]
dp[0][2] = cost[0][2]

for i in range(1, n):
	dp[i][0] = cost[i][0] + min(dp[i-1][1], dp[i-1][2])
	dp[i][1] = cost[i][1] + min(dp[i-1][0], dp[i-1][2])
	dp[i][2] = cost[i][2] + min(dp[i-1][1], dp[i-1][0])

print(min(dp[n-1]))


# 빨간색을 선택할 때, 직전에 파란색을 선택하면서 최소합만 모아놓은 것과 초록색을 선택하면서 최소합을 모아놓은 것을 비교하여 작은 것을 선택
