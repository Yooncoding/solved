"""
1978 - 소수찾기
https://www.acmicpc.net/problem/1978
"""

from sys import stdin
input = stdin.readline

def isPrime(n):
	if n == 1:
		return False
	for j in range(2, int(n**0.5)+1):
		if n % j == 0:
			return False
	return True

N = int(input())
arr = list(map(int, input().split()))
print(len([n for n in arr if isPrime(n)]))