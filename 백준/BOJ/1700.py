"""
1700 - 멀티탭 스케줄링
https://www.acmicpc.net/problem/1700
"""

from sys import stdin
from collections import deque

input = stdin.readline

n, k = map(int, input().rsplit())
order = deque(list(map(int, input().rsplit())))
multitap = []
ans = 0
while len(order) and len(multitap) < n:
    product = order.popleft()
    if product not in multitap:
        multitap.append(product)

for i in range(len(order)):
    visited = []

    if order[i] in multitap:
        continue

    for j in range(i, len(order)):
        if order[j] in multitap and order[j] not in visited:
            visited.append(order[j])

        if len(visited) == n - 1:
            break

    for k in multitap:
        if k not in visited:
            multitap.remove(k)
            ans += 1
            multitap.append(order[i])
            break

print(ans)
