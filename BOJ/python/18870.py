"""
18870 - 좌표 압축
https://www.acmicpc.net/problem/18870
"""

from sys import stdin

input = stdin.readline

n = int(input())
nums = list(map(int, input().rsplit()))
sorted_nums = list(set(nums))
sorted_nums.sort()

points = {sorted_nums[i]: i for i in range(len(sorted_nums))}

for i in nums:
    print(points[i], end=" ")
