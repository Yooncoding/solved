"""
1065 - 한수
https://www.acmicpc.net/problem/1065
"""

from sys import stdin
input = stdin.readline

a = int(input())
count = 0
if a <= 99:
    count = a
else:
    for i in range(100, a + 1):
        i = str(i)
        if int(i[0]) - int(i[1]) == int(i[1]) - int(i[2]):
            count += 1
    count += 99
print(count)
