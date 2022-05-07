"""
1747 - 소수&팰린드롬
https://www.acmicpc.net/problem/1747
"""

from sys import stdin
input = stdin.readline

def isPalendrom(p):
    number = str(p)
    mid = len(number) // 2
    for j in range(mid):
        if number[j] != number[-1 - j]:
            return False
    return True

def solution(arr):
    for i in arr:
        if isPalendrom(i) == False:
            continue
        return i


n = int(input())

arr = [False, False] + [True] * 999999
for i in range(2, 1001):
    if arr[i]:
        for j in range(i * 2, len(arr), i):
            arr[j] = False
data = [i for i in range(n, 1000001) if arr[i]]

result = solution(data)
# 반복문은 백만까지만 돌기 때문에 백만 이후 소수이며 가장 작은 팰린드롬 수 예외 처리
if result == None:
    result = 1003001

print(result)
