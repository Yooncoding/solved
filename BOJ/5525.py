"""
5525 - IOIOI
https://www.acmicpc.net/problem/5525
"""

from sys import stdin

input = stdin.readline

n = int(input())
m = int(input())
s = input().rstrip()

i = 1
cnt, ans = 0, 0
while i < m - 1:
    if s[i] == "O" and s[i - 1] == "I" and s[i + 1] == "I":
        cnt += 1
        i += 1
    else:
        if cnt >= n:
            ans += (cnt - n + 1)
        cnt = 0
    i += 1

# 남은 cnt 처리
if cnt >= n:
    ans += (cnt - n + 1)
print(ans)
