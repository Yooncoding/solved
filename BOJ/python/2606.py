"""
2606 - 바이러스
https://www.acmicpc.net/problem/2606
"""

from sys import stdin
from collections import deque

input = stdin.readline

N = int(input())
M = int(input())
result = [False] * (N + 1)
result[1] = True

network = dict()
for i in range(1, N + 1):
    network[i] = set()

for _ in range(M):
    a, b = map(int, input().split())
    network[a].add(b)
    network[b].add(a)

queue = deque([1])
while queue:
    i = queue.popleft()
    if result[i] == True:
        for j in network[i]:
            if result[j] == False:
                result[j] = True
                queue.append(j)

print(result.count(True) - 1)
