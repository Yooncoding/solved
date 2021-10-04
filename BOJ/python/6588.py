"""
6588 - 골드바흐의 추측
https://www.acmicpc.net/problem/6588
"""

from sys import stdin
input = stdin.readline


def solution(arr, n):
    for j in range(n // 2 + 1):
        if arr[n - j] is True and arr[j] is True:
            return [j, n - j]


arr = [False, False] + [True] * 999999
for i in range(2, 1001):
    if arr[i]:
        for j in range(i * 2, len(arr), i):
            arr[j] = False

while True:
    n = int(input())
    if n == 0:
        break
    result = solution(arr, n)
    if result:
        answer = str(n) + " = " + str(result[0]) + " + " + str(result[1])
    else:
        answer = "Goldbach's conjecture is wrong."
    print(answer)