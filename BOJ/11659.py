"""
11659 - 구간 합 구하기 4
https://www.acmicpc.net/problem/11659
"""

from sys import stdin

input = stdin.readline

n, m = map(int, input().rsplit())
nums = list(map(int, input().rsplit()))

for i in range(1, n):
    nums[i] += nums[i - 1]

for _ in range(m):
    i, j = map(int, input().rsplit())
    if i == 1:
        print(nums[j-1])
        continue

    print(nums[j-1] - nums[i-2])
