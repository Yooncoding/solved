"""
10816 - 숫자카드2
https://www.acmicpc.net/problem/10816
"""

from sys import stdin
input = stdin.readline

def solution(card, check):
    collection = dict()
    for i in check:
        collection[i] = 0
    for j in card:
        if j in collection:
            collection[j] += 1
    return collection


n = int(input())
card = list(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))
result = solution(card, check)

for k in check:
    print(result[k], end=" ")
