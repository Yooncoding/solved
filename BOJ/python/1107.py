"""
1107 - 리모컨
https://www.acmicpc.net/problem/1107
"""

from sys import stdin

input = stdin.readline

N = int(input())
M = int(input())
nums = list(map(int, input().split()))
broken = [False] * 10
for num in nums:
    broken[num] = True

cnt = N - 100 if N >= 100 else 100 - N

for i in range(1000000):
    processing = True
    temp = str(i)
    for t in temp:
        if broken[int(t)] == True:
            processing = False
            break
    if processing == False:
        continue
    cnt = min(cnt, i - N +
              len(temp)) if i >= N else min(cnt, N - i + len(temp))

print(cnt)
