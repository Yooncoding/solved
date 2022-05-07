"""
4949 - 균형잡힌 세상
https://www.acmicpc.net/problem/4949
"""

import sys

match = {")": "(", "]": "["}

while True:
    data = sys.stdin.readline().rstrip()
    stack = []
    status = True
    if data == ".":
        break
    for c in data:
        if c in "([":
            stack.append(c)
        elif c in match:
            if len(stack) == 0:
                status = False
            else:
                bracket = stack.pop()
                if bracket != match[c]:
                    status = False
        elif c == ".":
            if status == True and len(stack) == 0:
                print("yes")
            else:
                print("no")