"""
10866 - 덱
https://www.acmicpc.net/problem/10866
"""

from sys import stdin

input = stdin.readline

deq = []
for _ in range(int(input())):
    line = input().rsplit()
    if line[0] == "push_front":
        deq.insert(0, line[1])
    if line[0] == "push_back":
        deq.append(line[1])
    if line[0] == "size":
        print(len(deq))
    if line[0] == "empty":
        print(1 if len(deq) == 0 else 0)
    if line[0] == "pop_front":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.pop(0))
    if line[0] == "pop_back":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.pop())
    if line[0] == "front":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
    if line[0] == "back":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])
