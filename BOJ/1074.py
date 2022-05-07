"""
1074 - Z
https://www.acmicpc.net/problem/1074
"""

n, r, c = map(int, input().rsplit())
cnt = 0

while not (r == 0 and c == 0):
    size = 2**(n - 1)
    if 0 <= c < size and 0 <= r < size:
        cnt += size * size * 0

    elif size <= c < size * 2 and 0 <= r < size:
        c -= size
        cnt += size * size * 1

    elif 0 <= c < size and size <= r < size * 2:
        r -= size
        cnt += size * size * 2

    elif size <= c < size * 2 and size <= r < size * 2:
        c -= size
        r -= size
        cnt += size * size * 3

    n -= 1

print(cnt)
