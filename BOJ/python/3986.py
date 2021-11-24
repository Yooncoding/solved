"""
3986 - 좋은 단어
https://www.acmicpc.net/problem/3986
"""

from sys import stdin
input = stdin.readline

cnt = 0
for _ in range(int(input())):
    word = input().rstrip()
    stack = []
    for c in word:
        if len(stack) == 0:
            stack.append(c)
        else:
            peek = stack[-1]
            if peek == c:
                stack.pop()
            else:
                stack.append(c)
    if len(stack) == 0:
        cnt += 1

print(cnt)
