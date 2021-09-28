"""
2960 - 에라토스테네스의 체
https://www.acmicpc.net/problem/2960
"""

from sys import stdin
input = stdin.readline

def solution(n, k):
    arr = [False, False] + [True] * (n - 1)
    cnt = 0
    for i in range(2, n + 1):
        for j in range(i, len(arr), i):
            if arr[j]:
                arr[j] = False
                cnt += 1
                if cnt == k:
                    return j


n, k = map(int, input().split())
print(solution(n, k))
