"""
17608 - 막대기
https://www.acmicpc.net/problem/17608
"""

from sys import stdin

input = stdin.readline

stack = []
max_value = 0
cnt = 0

for _ in range(int(input())):
    stack.append(int(input()))

while len(stack) != 0:
    n = stack.pop()
    if n > max_value:
        cnt += 1
        max_value = n

print(cnt)




