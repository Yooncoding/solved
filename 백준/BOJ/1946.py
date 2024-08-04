"""
1946 - 신입 사원
https://www.acmicpc.net/problem/1946
"""

from sys import stdin

input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    scores = []
    for _ in range(n):
        document, interview = map(int, input().rsplit())
        scores.append((document, interview))

    scores.sort()

    ans = 0
    cut_line = scores[0][1]
    for document, interview in scores:
        if interview > cut_line:
            continue

        ans += 1
        cut_line = interview

    print(ans)
