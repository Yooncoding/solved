"""
23842 - 성냥개비 (INU 코드페스티벌 2021)
https://www.acmicpc.net/problem/23842
"""

from sys import stdin

input = stdin.readline

N = int(input())

answer = 'impossible'
counts = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}

for i in range(100):
    for j in range(100):
        if i + j >= 100:
            break
        a, b = i // 10, i % 10
        c, d = j // 10, j % 10
        e, f = (i + j) // 10, (i + j) % 10
        form = counts[a] + counts[b] + counts[c] + counts[d] + counts[
            e] + counts[f]
        if form == N - 4:
            answer = '{}{}+{}{}={}{}'.format(a, b, c, d, e, f)

print(answer)
