"""
11723 - 집합
https://www.acmicpc.net/problem/11723
"""

from sys import stdin
from collections import defaultdict

input = stdin.readline

setdict = defaultdict(int)

for _ in range(int(input())):
    cmd = input().rsplit()
    if cmd[0] == "add":
        setdict[int(cmd[1])] = 1
    if cmd[0] == "remove":
        setdict[int(cmd[1])] = 0
    if cmd[0] == "check":
        print(setdict[int(cmd[1])])
    if cmd[0] == "toggle":
        setdict[int(cmd[1])] = 1 if setdict[int(cmd[1])] == 0 else 0
    if cmd[0] == "all":
        for i in range(1, 21):
            setdict[i] = 1
    if cmd[0] == "empty":
        for i in range(1, 21):
            setdict[i] = 0
