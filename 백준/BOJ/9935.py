"""
9935 - 문자열 폭발
https://www.acmicpc.net/problem/9935
"""

from sys import stdin

input = stdin.readline

sentence = input().rstrip()
bomb = list(input().rstrip())

stack = []

for char in sentence:
    stack.append(char)
    if bomb[-1] == char:
        if stack[-len(bomb):] == bomb:
            for _ in range(len(bomb)):
                stack.pop()

if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack))
