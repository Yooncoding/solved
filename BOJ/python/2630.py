"""
2630 - 색종이 만들기
https://www.acmicpc.net/problem/2630
"""

from sys import stdin

input = stdin.readline

n = int(input())
paper = []
blue, white = 0, 0

for _ in range(n):
    paper.append(list(map(int, input().rsplit())))


def cut(y=0, x=0, n=n):
    global blue, white
    for i in range(n):
        for j in range(n):
            if paper[y][x] != paper[y+i][x+j]:
                cut(y, x, n//2)
                cut(y + n//2, x, n//2)
                cut(y, x + n//2, n//2)
                cut(y+n//2, x+n//2, n//2)
                return
    if paper[y][x] == 1:
        blue += 1
    else:
        white += 1
    return


cut()
print(white)
print(blue)
