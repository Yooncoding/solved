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

process = False
while not process and len(order):
    for i in range(n):
        if order[i] not in multitap:
            process = True
            break
    if process:
        break
    for _ in range(n):
        order.popleft()
if process:
    for i in range(len(order)):
        visited = []
        for j in range(i, len(order)):
            if order[j] in multitap and order[j] not in visited:
                visited.append(order[j])

            if len(visited) == n-1:
                break

        if order[i] in multitap:
            continue

        for k in multitap:
            if k not in visited:
                multitap.remove(k)
                ans += 1
                multitap.append(order[i])
                break


print(ans)
