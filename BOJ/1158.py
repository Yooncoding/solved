"""
1158 - 요세포스 문제
https://www.acmicpc.net/problem/1158
"""

import sys

n,k = list(map(int,sys.stdin.readline().rsplit()))
data = []
result = []
for i in range(n):
  data.append(i + 1)

temp_index = 0
while len(data) > 0:
  temp_index = (temp_index+(k-1)) % len(data)
  temp_value = data.pop(temp_index)
  result.append(str(temp_value))

print("<"+", ".join(result)+">")