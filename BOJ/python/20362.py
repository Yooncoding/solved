"""
20362 - 유니대전 퀴즈쇼 (INU 코드페스티벌 2020)
https://www.acmicpc.net/problem/20361
"""

from sys import stdin

input = stdin.readline

N, winner = input().split()
log = []
for _ in range(int(N)):
	nickname, answer = input().split()
	if nickname == winner:
		break
	log.append(answer)
    
print(log.count(answer))
