"""
1094 - 막대기
https://www.acmicpc.net/problem/1094
"""

from sys import stdin
input = stdin.readline

x = int(input())
stick = 64
cnt = 0
while stick != 0:
    if x >= stick:
        x = x - stick
        cnt = cnt + 1
    stick = stick / 2
print(cnt)
