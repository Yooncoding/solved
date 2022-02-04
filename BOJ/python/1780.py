"""
1780 - 종이의 개수
https://www.acmicpc.net/problem/1780
"""

from sys import stdin

input = stdin.readline

n = int(input())
paper = []
answer = [0, 0, 0]

for _ in range(n):
    paper.append(list(map(int, input().rsplit())))


def cut(y, x, n):
    global answer
    for i in range(n):
        for j in range(n):
            if paper[y][x] != paper[y+i][x+j]:
                n //= 3
                cut(y, x, n)
                cut(y+n, x, n)
                cut(y+2*n, x, n)
                cut(y, x+n, n)
                cut(y, x+2*n, n)
                cut(y+n, x+n, n)
                cut(y+2*n, x+n, n)
                cut(y+n, x+2*n, n)
                cut(y+2*n, x+2*n, n)
                return
    answer[paper[y][x]+1] += 1
    return


cut(0, 0, n)
print(*answer, sep="\n")
