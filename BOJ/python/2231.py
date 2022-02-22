"""
2231 - 분해합
https://www.acmicpc.net/problem/2231
"""

from sys import stdin

input = stdin.readline

n = input().rstrip()
length = len(n)
n = int(n)
min_v = n-length*9 if n > length*9 else 0
for i in range(min_v, n+1):
    tsum = i
    for j in str(i):
        tsum += int(j)
    if tsum == n:
        print(i)
        break
else:
    print(0)
