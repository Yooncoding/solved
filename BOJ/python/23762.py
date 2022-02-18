"""
23762 - 배드민턴 복식 팀 만들기
https://www.acmicpc.net/problem/23762
"""

from sys import stdin

input = stdin.readline

n = int(input())
nums = list(map(int, input().rsplit()))

ability = [[0, 0] for _ in range(n+1)]

for i in range(1, n+1):
    ability[i][0] = nums[i-1]
    ability[i][1] = i - 1

ability.sort()

dp = [0 for _ in range(n+1)]
out = [[] for _ in range(n+1)]
out[1].append(ability[1][1])
out[2].append(ability[1][1])
out[2].append(ability[2][1])


for i in range(4, n+1):
    gap = ability[i][0] - ability[i-3][0]
    if i % 4:
        dp[i] = min(dp[i-1], dp[i-4] + gap)

        if dp[i] == dp[i-1]:
            for o in out[i-1]:
                out[i].append(o)
            out[i].append(ability[i][1])
        else:
            for o in out[i-4]:
                out[i].append(o)
    else:
        dp[i] = dp[i-4] + gap

print(dp[n])

if n % 4:
    for o in out[n]:
        print(o)
