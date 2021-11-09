"""
1026 - 보물
https://www.acmicpc.net/problem/1026
"""

from sys import stdin
input = stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = 0

a.sort()
b.sort(reverse=True)

for i in range(n):
    result += (a[i] * b[i])

print(result)