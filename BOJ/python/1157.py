"""
1157 - 단어공부
https://www.acmicpc.net/problem/1157
"""

from sys import stdin
import collections

input = stdin.readline

counts = collections.defaultdict(int)
strs = input().rstrip().upper()

for c in strs:
    counts[c] += 1

max_value = [k for k, v in counts.items() if max(counts.values()) == v]

if len(max_value) > 1:
    print("?")
else:
    print(max_value[0])
