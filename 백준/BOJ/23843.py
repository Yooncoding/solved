"""
23843 - 콘센트 (INU 코드페스티벌 2021)
https://www.acmicpc.net/problem/23843
"""

from sys import stdin

input = stdin.readline

N, M = map(int, input().split())
answer = 0
times = sorted(list(map(int, input().split())))
charged = []

while len(times) != 0:
    while len(charged) != M:
        if len(times) == 0:
            break
        charged.append(times.pop())
    min_charged = min(charged)
    charged.remove(min_charged)
    for i in range(len(charged)):
        charged[i] = charged[i] - min_charged
    answer += min_charged

if len(charged):
    answer += max(charged)

print(answer)
