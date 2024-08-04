"""
2805 - 나무 자르기
https://www.acmicpc.net/problem/2805
"""

n, m = map(int, input().rsplit())
length = list(map(int, input().rsplit()))
max_length = max(length)
min_length = (sum(length) - m) // n

left, right = min_length, max_length
while left <= right:
    tsum = 0
    mid = (left + right) // 2
    for i in range(n):
        if length[i] < mid:
            continue
        tsum += (length[i] - mid)
    if tsum >= m:
        left = mid + 1
    else:
        right = mid - 1

print(right)
