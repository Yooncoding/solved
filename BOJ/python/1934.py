"""
1934 - 최소공배수
https://www.acmicpc.net/problem/1934
"""
from sys import stdin

input = stdin.readline

def gcd(a, b):
    if b > a:
        a, b = b, a
    return gcd(b, a % b) if b else a

def lms(a, b):
    return a * b // gcd(a, b)


for _ in range(int(input())):
    a, b = map(int, input().split())
    print(lms(a, b))
