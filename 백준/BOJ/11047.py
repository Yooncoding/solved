"""
11047 - 동전 0
https://www.acmicpc.net/problem/11047
"""

from sys import stdin

input = stdin.readline

n, k = map(int, input().rsplit())
coins = []
for _ in range(n):
    coins.append(int(input()))
coins = coins[::-1]

cnt = 0
for coin in coins:
    if k == 0:
        break
    if coin > k:
        continue
    cnt += (k // coin)
    k %= coin

print(cnt)
