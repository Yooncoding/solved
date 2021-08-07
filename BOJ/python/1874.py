"""
1873 - 스택수열
https://www.acmicpc.net/problem/1873
"""

import sys

n = int(sys.stdin.readline())


def solution(n):
    count, temp = 1, 1
    stack = []
    result = []
    status = True
    for _ in range(n):
        data = int(sys.stdin.readline())
        if data >= temp:
            while data >= temp:
                stack.append(count)
                result.append("+")
                count += 1
                temp = count
            temp = stack.pop()
            result.append("-")
        if data < temp:
            if stack[-1] == data:
                temp = stack.pop()
                result.append("-")
            else:
                status = False
    if status:
        return result
    else:
        return False


answer = solution(n)
if answer:
    for c in answer:
        print(c)
else:
    print("NO")
