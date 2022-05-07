"""
9613 - GCD 합
https://www.acmicpc.net/problem/9613
"""

from sys import stdin
from itertools import combinations
from math import gcd

input = stdin.readline

for _ in range(int(input())):
	N, *arr = map(int, input().split())
	values = list(combinations(arr, 2))
	ans = 0
	for value in values:
		ans += gcd(value[0], value[1])
	print(ans)
		