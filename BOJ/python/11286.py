"""
11286 - 절댓값 힙
https://www.acmicpc.net/problem/11286
"""

from sys import stdin
import heapq

input = stdin.readline

heap = []
for N in range(int(input())):
    x = int(input())
    if x == 0:
        if len(heap):
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(x), x))
