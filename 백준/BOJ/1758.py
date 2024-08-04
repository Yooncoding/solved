"""
1758 - 알바생 강호
https://www.acmicpc.net/problem/1758
"""


from sys import stdin

input = stdin.readline

n = int(input())
tips = []
for _ in range(n):
    tips.append(int(input()))
tips.sort(reverse=True)

time = 0
ans = 0
for tip in tips:
    time += 1
    cnt = tip - (time - 1)
    if cnt < 0:
        break
    ans += cnt

print(ans)
