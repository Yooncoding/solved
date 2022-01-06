"""
5430 - AC
https://www.acmicpc.net/problem/5430
"""

from sys import stdin
from collections import deque

input = stdin.readline

for _ in range(int(input())):
    p = input()
    n = int(input())
    x = input().rstrip()

    x = deque(map(int, x[1:-1].split(","))) if n != 0 else []

    reverse_flag, error_flag = False, False

    for c in p:
        if c == "R":
            if reverse_flag == True:
                reverse_flag = False
                continue
            reverse_flag = True
        elif c == "D":
            if len(x) == 0 or n == 0:
                print('error')
                error_flag = True
                break
            if reverse_flag == True:
                x.pop()
            elif reverse_flag == False:
                x.popleft()

    if error_flag == True:
        continue

    if reverse_flag == True:
        x.reverse()

    print(str(list(x)).replace(' ', ''))
