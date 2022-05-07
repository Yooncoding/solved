"""
3036 - 링
https://www.acmicpc.net/problem/3036
"""
from sys import stdin

input = stdin.readline

def gcd(a, b):
    if b > a:
        a, b = b, a
    return gcd(b, a % b) if b else a


N = int(input())
arr = list(map(int, input().split()))
for i in range(1, N):
	g = gcd(arr[0], arr[i])
	a = arr[0] // g
	b = arr[i] // g
	print(str(a)+"/"+str(b))