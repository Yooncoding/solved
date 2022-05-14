"""
2109 - 순회강연
https://www.acmicpc.net/problem/2109
"""

from sys import stdin

input = stdin.readline

n = int(input())
schedule = []
final = 0

for _ in range(n):
    pay, day = map(int, input().rsplit())
    final = max(final, day)
    schedule.append((pay, day))

schedule.sort(key=lambda x: (x[0], x[1]))

work_table = [0 for _ in range(final+1)]
while len(schedule):
    pay, day = schedule.pop()
    for i in range(day, 0, -1):
        if work_table[i] == 0:
            work_table[i] = pay
            break

print(sum(work_table))
