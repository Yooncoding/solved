"""
1931 - 회의실 배정
https://www.acmicpc.net/problem/1931
"""

from sys import stdin

input = stdin.readline

N = int(input())

timetable = []

for _ in range(N):
    timetable.append(list(map(int, input().rsplit())))

timetable.sort(key=lambda x: (x[1], x[0]))

prev_end = 0
cnt = 0
for t in timetable:
    start, end = t
    if prev_end > start:
        continue
    prev_end = end
    cnt += 1
print(cnt)
