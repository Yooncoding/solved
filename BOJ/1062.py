"""
1062 - 가르침
https://www.acmicpc.net/problem/1062
"""

from sys import stdin
from itertools import combinations

input = stdin.readline

n, k = map(int, input().rsplit())
words = []
alphabets = set()

for _ in range(n):
    word = input().rstrip()
    word = word[4:len(word) - 4]
    for alphabet in word:
        if alphabet not in "antic":
            alphabets.add(alphabet)
    words.append(word)

if k < 5:
    print(0)
    exit()
elif k == 26:
    print(n)
    exit()

combi_selection = len(alphabets)
if k - 5 <= combi_selection:
    combi_selection = k - 5

ans = 0
for combi in list(combinations(alphabets, combi_selection)):
    cnt = 0
    learned = set(["a", "n", "t", "i", "c"])
    for case in combi:
        learned.add(case)
    for word in words:
        for alphabet in word:
            if alphabet not in learned:
                break
        else:
            cnt += 1
    ans = max(ans, cnt)

print(ans)
