"""
12851 - 숨박꼭질 2
https://www.acmicpc.net/problem/12851
"""

from collections import deque

n, k = map(int, input().rsplit())
visited = [False for _ in range(100001)]
q = deque()
q.append((n, 0))
min_cnt = 0
path_cnt = 0
while len(q):
    n, cnt = q.popleft()

    if min_cnt != 0 and min_cnt < cnt:
        break

    if n == k:
        if min_cnt == 0:
            min_cnt = cnt
        if cnt == min_cnt:
            path_cnt += 1

    for i in [n + 1, n - 1, n * 2]:
        if 0 <= i <= 100000 and not visited[i]:
            q.append((i, cnt + 1))

    visited[n] = True

print(min_cnt)
print(path_cnt)
