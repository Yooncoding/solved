"""
2504 - 괄호의 값
https://www.acmicpc.net/problem/2504
"""

import sys


def checkBracket(S):
    stack = []
    match = {")": "(", "]": "["}
    for c in S:
        if c in "([":
            stack.append(c)
        elif c in match:
            if len(stack) == 0:
                return False
            else:
                t = stack.pop()
                if t != match[c]:
                    return False
    return len(stack) == 0


def solution(S):
    stack = []
    for c in S:
        if c in "([":
            stack.append(c)
        elif c == ")" and stack[-1] == "(":
            stack.pop()
            stack.append(2)
        elif c == ")" and type(stack[-1]) == int:
            temp = 0
            while stack[-1] != "(":
                temp += stack.pop()
                if len(stack) == 0:
                    break
            stack.pop()
            temp *= 2
            stack.append(temp)
        elif c == "]" and stack[-1] == "[":
            stack.pop()
            stack.append(3)
        elif c == "]" and type(stack[-1]) == int:
            temp = 0
            while stack[-1] != "[":
                temp += stack.pop()
                if len(stack) == 0:
                    break
            stack.pop()
            temp *= 3
            stack.append(temp)
    return sum(stack)


data = sys.stdin.readline().rstrip()
if checkBracket(data):
    print(solution(data))
else:
    print(0)