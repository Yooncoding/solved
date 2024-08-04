"""
2437 - 저울
https://www.acmicpc.net/problem/2437
"""

from sys import stdin

input = stdin.readline

n = int(input())

weights = list(map(int, input().rsplit()))
weights.sort()
target = 1
for weight in weights:
    if target < weight:
        break
    target += weight
print(target)
