from sys import stdin

input = stdin.readline

n, k = map(int, input().rsplit())

items = [[0, 0]] + [list(map(int, input().rsplit())) for _ in range(n)]
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        w, v = items[i][0], items[i][1]

        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)

print(dp[n][k])
