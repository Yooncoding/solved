"""
1850 - 최대공약수
https://www.acmicpc.net/problem/1850
"""

from sys import stdin

input = stdin.readline

def gcd(a, b):
    if b > a:
        a, b = b, a
    return gcd(b, a % b) if b else a

A, B = map(int, input().split())
print('1' * gcd(A, B))