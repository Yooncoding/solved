"""
10773 - 제로
https://www.acmicpc.net/problem/10773
"""

import sys

k = int(sys.stdin.readline())
stack = []
for _ in range(k):
    n = int(sys.stdin.readline())
    if n != 0:
        stack.append(n)
    else:
        stack.pop()
print(sum(stack))
