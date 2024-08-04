"""
18870 - 좌표 압축
https://www.acmicpc.net/problem/18870
"""

from sys import stdin

input = stdin.readline

n = int(input())
x = list(map(int, input().rsplit()))
sorted_x = sorted(list(set(x)))

cnt = {sorted_x[i]: i for i in range(len(sorted_x))}

for i in x:
    print(cnt[i], end=" ")
