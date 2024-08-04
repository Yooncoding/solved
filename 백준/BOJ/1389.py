"""
1389 - 케빈 베이컨의 6단계 법칙
https://www.acmicpc.net/problem/1389
"""

from collections import defaultdict, deque


graph = defaultdict(list)
n, m = map(int, input().rsplit())

for _ in range(m):
    a, b = map(int, input().rsplit())
    graph[a].append(b)
    graph[b].append(a)


def bfs(v):
    visited = [False for _ in range(n + 1)]
    visited[v] = True
    cnt = [0 for _ in range(n + 1)]
    q = deque()
    q.append(v)
    while len(q):
        v = q.popleft()

        for t in graph[v]:
            if visited[t]:
                continue
            q.append(t)
            cnt[t] = cnt[v] + 1
            visited[t] = True

    return sum(cnt)


ans = []
for i in range(n):
    ans.append(bfs(i + 1))

print(ans.index(min(ans)) + 1)
