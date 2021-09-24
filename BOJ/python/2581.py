"""
2581 - 소수
https://www.acmicpc.net/problem/2581
"""

from sys import stdin
from math import sqrt
input = stdin.readline

def isPrime(x):
	for _ in range(1, x):
		if x == 1:
			return False
		for j in range(2,int(sqrt(x))+1):
			if x % j == 0:
				return False
		return True

arr = []
m = int(input())
n = int(input())
for i in range(m, n + 1):
	if isPrime(i):
		arr.append(i)
print(sum(arr)if len(arr) else -1)
print(arr[0] if len(arr) else '')