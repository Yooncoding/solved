"""
1992 - 쿼드트리
https://www.acmicpc.net/problem/1992
"""

from sys import stdin

input = stdin.readline

n = int(input())
matrix = []
ans = []
for _ in range(n):
    matrix.append(list(map(int, input().rstrip())))


def compression(size, y=0, x=0):
    for i in range(size):
        for j in range(size):
            if matrix[y][x] != matrix[y + i][x + j]:
                div = size // 2
                ans.append("(")
                compression(div, y, x)
                compression(div, y, x + div)
                compression(div, y + div, x)
                compression(div, y + div, x + div)
                ans.append(")")
                return
    ans.append(matrix[y][x])
    return


compression(n)
print(*ans, sep="")
