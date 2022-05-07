"""
9012 - 괄호
https://www.acmicpc.net/problem/9012
"""

import sys

t = int(sys.stdin.readline())
stack = []
status = True
for _ in range(t):
    data = input()
    for c in data:
        if c == "(":
            stack.append(c)
        if c == ")":
            if len(stack) == 0:
                status = False
                break
            stack.pop()
    if status:
        if len(stack) == 0:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
        status = True