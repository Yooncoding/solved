"""
1543 - 문서 검색
https://www.acmicpc.net/problem/1543
"""

from sys import stdin


input = stdin.readline

doc = input().rstrip()
word = input().rstrip()
ans = 0
i = 0
while i <= len(doc) - len(word):
    if doc[i:i + len(word)] == word:
        ans += 1
        i += len(word)
    else:
        i += 1
print(ans)
