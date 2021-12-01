"""
1966 - 프린터 큐
https://www.acmicpc.net/problem/1966
"""

from sys import stdin

input = stdin.readline

for _ in range(int(input())):
    N, M = list(map(int, input().split()))
    priority = list(map(int, input().split()))
    data = [i for i in range(N)]
    result = []

    while len(priority) != 0:
        if priority[0] != max(priority):
            priority.append(priority.pop(0))
            data.append(data.pop(0))
        else:
            priority.pop(0)
            result.append(data.pop(0))

    for i in range(N):
        if result[i] == M:
            print(i + 1)
            break
