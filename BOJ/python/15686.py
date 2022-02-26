"""
15686 - 치킨배달
https://www.acmicpc.net/problem/15686
"""

from sys import stdin
from math import inf
from itertools import combinations

input = stdin.readline

n, m = map(int, input().rsplit())
graph = [list(map(int, input().rsplit())) for _ in range(n)]
houses = []
chikens = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chikens.append((i, j))
        if graph[i][j] == 1:
            houses.append((i, j))

min_v = inf
for combi in combinations(chikens, m):
    sum_v = 0
    for house in houses:
        temp = 100
        for chiken in combi:
            dist = abs(chiken[0]-house[0]) + abs(chiken[1]-house[1])
            temp = min(temp, dist)
        sum_v += temp
    min_v = min(min_v, sum_v)

print(min_v)
