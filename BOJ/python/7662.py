"""
7662 - 이중 우선순위 큐
https://www.acmicpc.net/problem/7662
"""

import heapq
from sys import stdin

input = stdin.readline

for _ in range(int(input())):
    max_heap, min_heap = [], []
    visited = [False for _ in range(1000001)]
    for key in range(int(input())):
        cmd = input().rsplit()
        if cmd[0] == "I":
            heapq.heappush(min_heap, (int(cmd[1]), key))
            heapq.heappush(max_heap, (int(cmd[1]) * -1, key))
            visited[key] = True
        if cmd[0] == "D":
            if cmd[1] == "-1":
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
            if cmd[1] == "1":
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)

    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")
