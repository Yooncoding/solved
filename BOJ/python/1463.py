"""
1463 - 1로 만들기
https://www.acmicpc.net/problem/1463
"""

from sys import stdin
input = stdin.readline

x = int(input())
results = [x]
count = 0
while 1:
    if x == 1:
        break
    count += 1
    temp = results
    for i in range(len(temp)):
        results.append(temp[i] - 1)
        if temp[i] % 3 == 0:
            results.append(temp[i] // 3)
        if temp[i] % 2 == 0:
            results.append(temp[i] // 2)
        results = set(results)
        results = list(results)
    if min(results) == 1:
        break
print(count)
