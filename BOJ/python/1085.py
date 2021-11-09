"""
1085 - 직사각형에서 탈출
https://www.acmicpc.net/problem/1085
"""

from sys import stdin
input = stdin.readline

length = []
x, y, w, h = list(map(int, input().split()))

length.append(w - x)
length.append(h - y)
length.append(x)
length.append(y)

print(min(length))
