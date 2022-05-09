"""
그리디 문제
Q4 만들 수 없는 금액 (p.314)
"""

from sys import stdin

input = stdin.readline

n = int(input())

coins = list(map(int, input().rsplit()))
coins.sort()
target = 1
for coin in coins:
    if target < coin:
        break
    target += coin
print(target)
