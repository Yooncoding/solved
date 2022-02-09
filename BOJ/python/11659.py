"""
11659 - 구간 합 구하기 4
https://www.acmicpc.net/problem/11659
"""

from sys import stdin

input = stdin.readline

n, m = map(int, input().rsplit())
nums = list(map(int, input().rsplit()))
prefix_sums = [0]

temp = 0
for num in nums:
    temp += num
    prefix_sums.append(temp)


for _ in range(m):
    i, j = map(int, input().rsplit())
    print(prefix_sums[j]-prefix_sums[i-1])
