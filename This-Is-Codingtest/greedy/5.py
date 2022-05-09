"""
그리디 문제
Q5 볼링공 구하기 (p.315)
"""

from sys import stdin

input = stdin.readline

n, m = map(int, input().rsplit())
weights = list(map(int, input().rsplit()))
cnts = [0 for _ in range(m+1)]
for weight in weights:
    cnts[weight] += 1

ans = 0
for i in range(1, m+1):
    n -= cnts[i]
    ans += (cnts[i] * n)
print(ans)
