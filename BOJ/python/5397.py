"""
5397 - 키로거
https://www.acmicpc.net/problem/5397
"""

from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    log = input().rstrip()
    temp = []
    data = []
    for i in log:
        if i not in "-><":
            data.append(i)
        if len(data) != 0:
            if i == "<":
                temp.append(data.pop())
            if i == "-":
                data.pop()
        if i == ">" and len(temp) != 0:
            data.append(temp.pop())

    while len(temp) != 0:
        data.append(temp.pop())

    print("".join(map(str, data)))
