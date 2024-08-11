"""
https://softeer.ai/practice/6284
24-08-12
"""

import sys

input = sys.stdin.readline

k, p, n = map(int, input().rsplit())
mod = 1000000007

for _ in range(n):
    if k > mod:
        k %= mod
    k *= p

print(k % mod)
