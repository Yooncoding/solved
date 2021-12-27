"""
20361 - 일우는 야바위꾼 (INU 코드페스티벌 2020)
https://www.acmicpc.net/problem/20361
"""

from sys import stdin

input = stdin.readline

N, X, K = map(int, input().split())
cup = [0] * N
cup[X - 1] = 1
for _ in range(K):
    a, b = map(int, input().split())
    cup[a - 1], cup[b - 1] = cup[b - 1], cup[a - 1]
print(cup.index(1) + 1)
