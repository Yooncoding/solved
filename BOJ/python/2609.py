"""
2609 - 최대공약수와 최소공배수
https://www.acmicpc.net/problem/2609
"""

from sys import stdin
input = stdin.readline

def gcd(a, b):
	if b > a:
		a, b = b, a
	return gcd(b, a % b) if b else a

def lcm(a, b):
	return (a * b) // gcd(a, b)

a, b = map(int, input().split())
print(gcd(a, b), lcm(a, b))