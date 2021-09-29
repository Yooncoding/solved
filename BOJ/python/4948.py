"""
4948 - 베르트랑 공존
https://www.acmicpc.net/problem/4948
"""

from sys import stdin
input = stdin.readline

def solution(n):
    arr = [False, False] + [True] * ((n * 2) - 1)
    for i in range(2, int((n * 2)**0.5) + 1):
        if arr[i]:
            for j in range(i * 2, len(arr), i):
                arr[j] = False
    return arr[n + 1:n * 2 + 1].count(True)


while True:
    n = int(input())
    if n == 0:
        break
    print(solution(n))
