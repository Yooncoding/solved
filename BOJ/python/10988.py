"""
10988 - 팰린드롬인지 확인하기
https://www.acmicpc.net/problem/10988
"""

from sys import stdin
input = stdin.readline().rstrip

data = input()
ans = 1 if data == data[::-1] else 0
print(ans)