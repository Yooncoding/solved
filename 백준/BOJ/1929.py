"""
1929 - 소수 구하기
https://www.acmicpc.net/problem/1929
"""

from sys import stdin
input = stdin.readline

def eratosthenesSieve(m, n):
    arr = [False, False] + [True] * (n - 1)
    for i in range(2, int(n**0.5) + 1):
        if arr[i] == True:
            for j in range(i * 2, len(arr), i):
                arr[j] = False
    return [i for i in range(m, n + 1) if arr[i]]


m, n = map(int, input().split())
num = eratosthenesSieve(m, n)
print(*num, sep="\n")