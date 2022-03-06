"""
1931 - 회의실 배정
https://www.acmicpc.net/problem/1931
"""

from sys import stdin

input = stdin.readline

timetable = []
for N in range(int(input())):
    timetable.append(tuple(map(int, input().rsplit())))

timetable.sort(key=lambda x: (x[1], x[0]))

prev_end = -1
cnt = 0
for time in timetable:
    start, end = time
    if prev_end > start:
        continue
    cnt += 1
    prev_end = end

print(cnt)
