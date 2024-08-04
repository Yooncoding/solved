"""
1764 - 듣보잡
https://www.acmicpc.net/problem/1764
"""

from sys import stdin
from collections import defaultdict

input = stdin.readline

N, M = map(int, input().split())
names = defaultdict(bool)
answer = []
cnt = 0
for _ in range(M):
	names[input().rstrip()] = True

for _ in range(N):
	name = input().rstrip()
	if names[name] == True:
		answer.append(name)
		cnt += 1

answer.sort()

print(cnt)
for name in answer:
	print(name)