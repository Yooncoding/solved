"""
1463 - 1로 만들기
https://www.acmicpc.net/problem/1463
"""

from collections import deque

n = int(input())

q = deque()
q.append([n, 0])
visited = [False for _ in range(n+1)]
while len(q):
    n, cnt = q.popleft()
    if n == 1:
        print(cnt)
        break
    if not visited[n-1]:
        q.append([n-1, cnt+1])
        visited[n-1] = True
    if n % 3 == 0 and not visited[n//3]:
        visited[n//3] = True
        q.append([n//3, cnt+1])
    if n % 2 == 0 and not visited[n//2]:
        visited[n//2] = True
        q.append([n//2, cnt+1])
