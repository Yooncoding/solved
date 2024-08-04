"""
7662 - 이중 우선순위 큐
https://www.acmicpc.net/problem/7662
"""

from sys import stdin
import heapq

input = stdin.readline

for T in range(int(input())):
    id = 0
    maxheapq, minheapq = [], []
    visited = [False for _ in range(1000000)]
    for id in range(int(input())):
        comm = input().rsplit()
        n = int(comm[1])

        if comm[0] == "I":
            heapq.heappush(maxheapq, (-n, id))
            heapq.heappush(minheapq, (n, id))
            id += 1

        if comm[0] == "D":
            if n == 1 and len(maxheapq):
                m, i = heapq.heappop(maxheapq)
                while visited[i] and len(maxheapq):
                    m, i = heapq.heappop(maxheapq)
                visited[i] = True
            if n == -1 and len(minheapq):
                m, i = heapq.heappop(minheapq)
                while visited[i] and len(minheapq):
                    m, i = heapq.heappop(minheapq)
                visited[i] = True

    while len(minheapq) and visited[minheapq[0][1]]:
        heapq.heappop(minheapq)
    while len(maxheapq) and visited[maxheapq[0][1]]:
        heapq.heappop(maxheapq)

    if minheapq and maxheapq:
        print(-maxheapq[0][0], minheapq[0][0])
    else:
        print("EMPTY")
