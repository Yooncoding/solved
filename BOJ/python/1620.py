"""
1620 - 나는야 포켓몬 마스터 이다솜
https://www.acmicpc.net/problem/1620
"""

from sys import stdin

input = stdin.readline

N, M = map(int, input().split())
book = {}

for i in range(N):
    pocketmon = input().rstrip()
    book[i + 1] = pocketmon

reversed_book = dict(map(reversed, book.items()))

for _ in range(M):
    question = input().rstrip()
    if question.isdigit():
        answer = book[int(question)]
    else:
        answer = reversed_book[question]
    print(answer)