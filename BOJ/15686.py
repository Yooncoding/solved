"""
15686 - 치킨배달
https://www.acmicpc.net/problem/15686
"""

import math
from itertools import combinations

INF = math.inf

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
houses = []
restaurants = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            restaurants.append((i, j))
        if graph[i][j] == 1:
            houses.append((i, j))

ans = INF
for combination in combinations(restaurants, m):
    sum_dist = 0
    for house in houses:
        temp = 100
        for restaurant in combination:
            dist = abs(restaurant[0] - house[0]) + \
                abs(restaurant[1] - house[1])
            temp = min(temp, dist)
        sum_dist += temp
    ans = min(ans, sum_dist)

print(ans)
