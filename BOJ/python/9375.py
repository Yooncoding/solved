from sys import stdin
from collections import defaultdict

input = stdin.readline

for T in range(int(input())):
    clothes = defaultdict(int)
    cnt = 1

    for n in range(int(input())):
        name, kind = input().rsplit()
        clothes[kind] += 1

    for kind in clothes:
        cnt *= (clothes[kind] + 1)

    print(cnt - 1)
