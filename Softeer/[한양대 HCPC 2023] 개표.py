from sys import stdin

input = stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a, b = n // 5, n % 5
    print("++++ "*a + "|"*b)