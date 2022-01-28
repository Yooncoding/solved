"""
11047 - 동전 0
https://www.acmicpc.net/problem/11047
"""

from sys import stdin

input = stdin.readline

N, K = map(int, input().rsplit())
coin = []
cnt = 0

for _ in range(N):
    coin.append(int(input()))

while K != 0:
    b = K // coin[-1]
    if b > 0:
        cnt += b
        K = K % coin[-1]
    coin.pop()

print(cnt)
