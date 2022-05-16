"""
2170 - 선 긋기
https://www.acmicpc.net/problem/2170
"""

from sys import stdin


input = stdin.readline

n = int(input())

points = []
for _ in range(n):
    x, y = map(int, input().rsplit())
    points.append((x, y))
points.sort(key=lambda x: (x[0], x[1]))

ans = 0
low, high = points[0]

for i in range(1, len(points)):
    x, y = points[i]
    if high >= x:
        if high < y:
            high = y
        continue

    ans += (high-low)
    low, high = x, y

ans += (high-low)
print(ans)
