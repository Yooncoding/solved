"""
1406 - 에디터
https://www.acmicpc.net/problem/1406
"""

from sys import stdin
input = stdin.readline

data = list(input().rstrip())
m = int(input())
stack = []
for _ in range(m):
    line = input().rsplit()
    if line[0] == "L" and len(data) != 0:
        stack.append(data.pop())
    if line[0] == "P":
        data.append(line[1])
    if line[0] == "D" and len(stack) != 0:
        data.append(stack.pop())
    if line[0] == "B" and len(data) != 0:
        data.pop()
while len(stack) != 0:
    data.append(stack.pop())

print("".join(map(str, data)))