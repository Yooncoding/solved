"""
1181 - 단어정렬
https://www.acmicpc.net/problem/1181
"""

import sys

result = []
n = int(sys.stdin.readline())
for _ in range(n):
	data = sys.stdin.readline().rstrip()
	result.append(data)
result = list(set(result))
result.sort(key = lambda x: (len(x),x))
for i in result:
	print(i)