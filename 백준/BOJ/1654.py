"""
1654 - 랜선 자르기
https://www.acmicpc.net/problem/1654
"""

length = []
k, n = map(int, input().rsplit())
for _ in range(k):
    length.append(int(input()))

total = sum(length) // n

left, right = 1, total

while left <= right:
    tsum = 0
    mid = (left + right) // 2

    for i in range(k):
        tsum += (length[i] // mid)

    if tsum >= n:
        left = mid + 1
    else:
        right = mid - 1

print(right)
