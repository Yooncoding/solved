"""
10815 - 숫자카드
https://www.acmicpc.net/problem/10815
"""

from sys import stdin
input = stdin.readline

def solution(card, check):
	result = ""
	setCard = set(card)
	for j in check:
		if j in setCard:
			result += "1 "
		else:
			result += "0 "
	return result


n = int(input())
card = list(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))

print(solution(card, check))