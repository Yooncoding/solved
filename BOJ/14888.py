"""
14888 - 연산자 끼워넣기
https://www.acmicpc.net/problem/14888
"""

from sys import stdin
from math import inf

INF = inf
input = stdin.readline

n = int(input())
a = list(map(int, input().rsplit()))
op = list(map(int, input().rsplit()))
max_ans, min_ans = -INF, INF


def cal(opcode, a, b):
    if opcode == 0:
        return a + b
    elif opcode == 1:
        return a - b
    elif opcode == 2:
        return a * b
    else:
        if a * b >= 0:
            return a // b
        else:
            return -(abs(a) // abs(b))


def dfs(cnt, tans):
    global min_ans, max_ans
    if cnt == n - 1:
        max_ans = max(max_ans, tans)
        min_ans = min(min_ans, tans)
        return
    for opcode in range(4):
        if op[opcode] == 0:
            continue
        op[opcode] -= 1
        dfs(cnt + 1, cal(opcode, tans, a[cnt + 1]))
        op[opcode] += 1
    return


dfs(0, a[0])
print(max_ans, min_ans)
