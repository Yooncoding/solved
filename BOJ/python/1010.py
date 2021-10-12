"""
1010 - 다리 놓기
https://www.acmicpc.net/problem/1010
"""

from sys import stdin
input = stdin.readline

def factorial(x):
    return 1 if x <= 1 else x * factorial(x - 1)

def combi(n, m):
    return factorial(n) // (factorial(m) * factorial(n - m))


for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    print(combi(m, n))