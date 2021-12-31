"""
19583 - 싸이버개강총회
https://www.acmicpc.net/problem/19583
"""

from sys import stdin
from collections import defaultdict

input = stdin.readline

S, E, Q = input().split()
S = int(''.join(S.split(":")))
E = int(''.join(E.split(":")))
Q = int(''.join(Q.split(":")))

attendance = defaultdict(int)
cnt = 0

while True:
    info = input()
    if len(info) < 3:
        break
    log = info.rsplit()
    t = int(''.join(log[0].split(":")))
    n = log[1]
    if t <= S:
        attendance[n] += 1
    elif E <= t and t <= Q:
        if attendance[n] >= 1:
            attendance[n] = 0
            cnt += 1

print(cnt)
