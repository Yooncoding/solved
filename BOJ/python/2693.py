"""
2693 - N번째 큰 수
https://www.acmicpc.net/problem/2693
"""

from sys import stdin
input = stdin.readline

for _ in range(int(input())):
	arr = list(map(int, input().split()))
	arr.sort(reverse=True)
	print(arr[2])