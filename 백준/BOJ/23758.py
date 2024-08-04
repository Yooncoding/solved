"""
23758 - 중앙값 제거
https://www.acmicpc.net/problem/23758
"""

import math
from sys import stdin

input = stdin.readline

n = int(input())
cnt = 0
nums = list(map(int, input().rsplit()))
nums.sort()
nums = nums[:(n+1)//2]

for num in nums:
    cnt += int(math.log2(num))

print(cnt+1)
