"""
14719 - 빗물
https://www.acmicpc.net/problem/14719
"""

from sys import stdin

input = stdin.readline

h, w = map(int, input().rsplit())
block = list(map(int, input().rsplit()))
max_height = max(block)
max_height_idx = block.index(max_height)
left, right = 0, len(block)-1
left_max, right_max = 0, 0
ans = 0

while left < max_height_idx:
    left_max = max(left_max, block[left])
    ans += (left_max - block[left])
    left += 1

while right > max_height_idx:
    right_max = max(right_max, block[right])
    ans += (right_max - block[right])
    right -= 1

print(ans)
