"""
1735 - 분수 합
https://www.acmicpc.net/problem/1735
"""

from sys import stdin
input = stdin.readline

def gcd(a, b):
    return gcd(b, a % b) if b else a

def solution(a, b):
    result = []
    result.append(a // gcd(a, b))
    result.append(b // gcd(a, b))
    return result


n, m = map(int, input().split())
x, y = map(int, input().split())
a = (n * y) + (x * m)
b = m * y

result = solution(a, b)
print(result[0], result[1])
