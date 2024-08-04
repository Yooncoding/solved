"""
9020 - 골드바흐의 추측
https://www.acmicpc.net/problem/9020
"""

from sys import stdin
input = stdin.readline

def solution(arr, n):
    m = n // 2
    for j in range(m, 1, -1):
        if arr[n - j] is True and arr[j] is True:
            return [j, n - j]


arr = [False, False] + [True] * 9999
for i in range(2, 101):
    if arr[i]:
        for j in range(i * 2, len(arr), i):
            arr[j] = False

for _ in range(int(input())):
    n = int(input())
    result = solution(arr, n)
    print(result[0], result[1])
