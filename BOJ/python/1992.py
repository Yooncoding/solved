"""
1992 - 쿼드트리
https://www.acmicpc.net/problem/1992
"""

from sys import stdin

input = stdin.readline

n = int(input())
pixel = []
answer = ""

for _ in range(n):
    pixel.append(list(map(int, input().rstrip())))


def compression(y, x, n):
    global answer
    for i in range(n):
        for j in range(n):
            if pixel[y][x] != pixel[y+i][x+j]:
                answer += "("
                compression(y, x, n//2)
                compression(y, x+n//2, n//2)
                compression(y+n//2, x, n//2)
                compression(y+n//2, x+n//2, n//2)
                answer += ")"
                return
    answer += str(pixel[y][x])
    return


compression(0, 0, n)
print(answer)
