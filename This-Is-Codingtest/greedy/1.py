"""
그리디 문제
Q1 모험가 길드 (p.311)
"""

from sys import stdin

input = stdin.readline

n = input().rstrip()
nums = list(map(int, input().rsplit()))
nums.sort()
ans, cnt = 0, 0
for num in nums:
    cnt += 1
    if cnt >= num:
        ans += 1
        cnt = 0
print(ans)
