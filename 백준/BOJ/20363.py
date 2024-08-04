"""
20363 - 당근 키우기 (INU 코드페스티벌 2020)
https://www.acmicpc.net/problem/20363
"""

from sys import stdin

input = stdin.readline

X, Y = map(int, input().split())
print(X + Y + (min(X, Y) // 10))