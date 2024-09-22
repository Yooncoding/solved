from sys import stdin
from collections import defaultdict, deque

input = stdin.readline

n = int(input())
graph = defaultdict(list)

for _ in range(n-1):
    v1, v2 = map(int, input().rsplit())
    graph[v1].append(v2)
    graph[v2].append(v1)


answer = [0 for _ in range(n+1)]
def bfs():
    q = deque()
    q.append(1)

    while len(q):
        v = q.popleft()
        for nv in graph[v]:
            if nv == 1 or answer[nv] != 0:
                continue

            answer[nv] = v
            q.append(nv)

    return

bfs()
for i in range(2, n+1):
    print(answer[i])
