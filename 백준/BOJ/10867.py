"""
10867 - 중복 빼고 정렬하기
https://www.acmicpc.net/problem/10867
"""

from sys import stdin
input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr = list(set(arr))
arr.sort()
print(*arr)