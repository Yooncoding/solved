"""
https://softeer.ai/practice/6283
24-08-12
"""

import sys

input = sys.stdin.readline

gear = list(map(int, input().rsplit()))

asc = [1, 2, 3, 4, 5, 6, 7, 8]
dec = [8, 7, 6, 5, 4, 3, 2, 1]

ans = ""
if gear == asc:
    ans = "ascending"
elif gear == dec:
    ans = "descending"
else:
    ans = "mixed"

print(ans)