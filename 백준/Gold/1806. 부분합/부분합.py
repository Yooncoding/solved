from sys import stdin
from math import inf

input = stdin.readline
INF = inf
n, s = map(int, input().rsplit())
a = list(map(int, input().rsplit()))

ans = INF
left, right = 0, 1

if a[left] >= s:
	ans = 1
	
k = a[left] + a[right]
while left < n:
	if k < s and right < n - 1:
		right += 1
		k += a[right]
		continue
	if k >= s:
		ans = min(ans, right - left + 1)
	k -= a[left]
	left += 1

if ans == INF:
	print(0)
else:
	print(ans)