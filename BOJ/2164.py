"""
2164 - 카드2
https://www.acmicpc.net/problem/2164
"""

from sys import stdin
from collections import deque

input = stdin.readline

N = int(input())
data = deque()
for i in range(1, N + 1):
    data.append(i)
while len(data) != 1:
    data.popleft()
    if len(data) != 0:
        data.append(data.popleft())
print(list(data)[0])
