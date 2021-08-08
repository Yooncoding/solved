"""
1873 - 스택수열
https://www.acmicpc.net/problem/1873
수정 21-08-08
"""

import sys

n = int(sys.stdin.readline())
stack = []
result = []
count = 0
status = True
for _ in range(n):
    num = int(sys.stdin.readline())

    while count < num:
        count += 1
        stack.append(count)
        result.append("+")

    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        status = False

if not status:
    print("NO")
else:
    for i in result:
        print(i)