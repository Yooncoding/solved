"""
그리디 문제
Q3 문자열 뒤집기 (p.313)
"""

from sys import stdin

input = stdin.readline

s = input().rstrip()
cur = -1
ans = [0, 0]
for c in s:
    if cur == -1:
        cur = int(c)
        continue
    elif cur == int(c):
        continue
    ans[cur] += 1
    cur = 0 if cur == 1 else 1
ans[cur] += 1
print(min(ans))
