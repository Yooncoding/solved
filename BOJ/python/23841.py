"""
23841 - 데칼코마니 (INU 코드페스티벌 2021)
https://www.acmicpc.net/problem/23841
"""

from sys import stdin

input = stdin.readline

N, M = map(int, input().split())
paints = []

for _ in range(N):
    paint = input().rstrip()
    temp = ['.'] * M
    for i in range(M):
        if paint[i].isupper():
            temp[i] = paint[i]
            temp[M - i - 1] = paint[i]
    paints.append(temp)

for paint in paints:
    print("".join(paint))
