"""
17219 - 비밀번호 찾기
https://www.acmicpc.net/problem/17219
"""

from sys import stdin

input = stdin.readline

N, M = map(int, input().rsplit())
memo = {}
for _ in range(N):
    addr, pwd = input().rsplit()
    memo[addr] = pwd

for _ in range(M):
    addr = input().rstrip()
    print(memo[addr])
