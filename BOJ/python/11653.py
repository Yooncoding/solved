"""
11653 - 소인수분해
https://www.acmicpc.net/problem/11653
"""

from sys import stdin
input = stdin.readline

def factorization(n):
    if n == 1:
        return False
    for i in range(2, int(n**(1 / 2) + 1)):
        while n % i == 0:
            print(i)
            n /= i
    if n != 1:
        print(int(n))


n = int(input())
num = factorization(n)