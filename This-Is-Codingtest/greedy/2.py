"""
그리디 문제
Q2 곱하기 혹은 더하기 (p.312)
"""

from sys import stdin

input = stdin.readline

s = input().rstrip()
ans = 0
for c in s:
    num = int(c)
    if num <= 1 or ans <= 1:
        ans += num
    else:
        ans *= num
print(ans)
