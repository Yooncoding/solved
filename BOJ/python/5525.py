"""
5525 - IOIOI
https://www.acmicpc.net/problem/5525
"""

from sys import stdin

input = stdin.readline

N = int(input())
M = int(input())
S = input().rstrip()

i = 1
cnt = 0
res = 0
while i < M - 1:
    if S[i-1] == "I" and S[i] == "O" and S[i+1] == "I":
        cnt += 1
        if cnt == N:
            res += 1
            cnt -= 1
        i += 1
    else:
        cnt = 0
    i += 1

print(res)
