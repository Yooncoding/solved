"""
https://softeer.ai/practice/6288
24-08-12
"""

import sys

input = sys.stdin.readline

w, n = map(int, input().rsplit())
vault = [list(map(int, input().rsplit())) for _ in range(n)]

vault.sort(key=lambda x: x[1], reverse=True)

ans = 0
for m, p in vault:
    if w >= m:
        ans += (m * p)
        w -= m
    else:
        ans += (w * p)
        break

print(ans)