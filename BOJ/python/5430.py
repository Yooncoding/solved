"""
5430 - AC
https://www.acmicpc.net/problem/5430
"""

from sys import stdin
from collections import deque

input = stdin.readline

for T in range(int(input())):
    p = input().rstrip()
    n = int(input())
    arr = input().rstrip()

    x = deque(map(int, arr[1:-1].split(","))) if n != 0 else []

    flag = False
    ans = ""
    for com in p:
        if com == "R":
            flag = True if not flag else False
        if com == "D":
            if len(x) == 0:
                ans = "error"
                break
            if flag:
                x.pop()
            else:
                x.popleft()
    if ans == "error":
        print(ans)
    else:
        if flag:
            x.reverse()
        print(str(list(x)).replace(' ', ''))
