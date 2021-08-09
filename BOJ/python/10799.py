"""
10799 - 쇠막대기
https://www.acmicpc.net/problem/10799
"""

import sys

data = sys.stdin.readline()
stack = []
result = 0
for i in range(len(data)):
    if data[i] == "(":
        stack.append(data[i])
    elif data[i] == ")":
        stack.pop()
        if data[i - 1] == "(":
            result += len(stack)
        else:
            result += 1
print(result)
