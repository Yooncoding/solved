"""
20364 - 부동산 다툼 (INU 코드페스티벌 2020)
https://www.acmicpc.net/problem/20364
"""

from sys import stdin

input = stdin.readline

N, Q = map(int, input().split())
arr = [0] + [0] * (N)

for i in range(Q):
    X = int(input())
    j = X
    check = True
    while j != 1:
        if arr[j]:
            check = False
            temp = j
        j = j // 2
    if not check:
        print(temp)
    else:
        arr[X] = 1
        print(0)
