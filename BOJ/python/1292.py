"""
1292 - 쉽게 푸는 문제
https://www.acmicpc.net/problem/1292
"""

from sys import stdin
input = stdin.readline

arr = []
for i in range(46):
	arr += [i] * i
a, b = map(int, input().split())
print(sum(arr[a-1:b]))