"""
그리디 문제
Q6 무지의 먹방 라이브 (p.316)
"""

from sys import stdin
import heapq

input = stdin.readline


food_times = list(map(int, input().rsplit()))
k = int(input())
ans = -1
heap = []
for i in range(len(food_times)):
    heapq.heappush(heap, (food_times[i], i))

prev = 0
n = len(food_times)

while len(heap):
    eat_time = (heap[0][0] - prev) * n
    if eat_time <= k:
        k -= eat_time
        prev, _ = heapq.heappop(heap)
        n -= 1
    else:
        heap.sort(key=lambda x: x[1])
        idx = k % n
        ans = heap[idx][1] + 1
        break

print(ans)
