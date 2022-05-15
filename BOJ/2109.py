"""
2109 - 순회강연
https://www.acmicpc.net/problem/2109
"""

from sys import stdin
import heapq

input = stdin.readline

n = int(input())
schedule = []
for _ in range(n):
    pay, day = map(int, input().rsplit())
    schedule.append((pay, day))

schedule.sort(key=lambda x: x[1])

work_table = []
for pay, day in schedule:
    if len(work_table) < day:
        heapq.heappush(work_table, pay)
    else:
        heapq.heappush(work_table, pay)
        heapq.heappop(work_table)

print(sum(work_table))
