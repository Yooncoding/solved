from sys import stdin
from collections import deque


input = stdin.readline

a, b = map(int, input().rsplit())
visited = set()

def bfs(s, t):
    q = deque()
    q.append([s, 0])

    while len(q):
        n, cnt = q.popleft()
        next_values = [2 * n, int(str(n)+"1")]

        for nn in next_values:
            if 1 <= nn < int(1e9) + 1 and nn not in visited:
                q.append([nn, cnt + 1])
                visited.add(nn)

            if nn == t:
                return cnt + 1 + 1 # 연산의 최솟값에 1을 더한 값

    return -1

visited.add(a)
result = bfs(a, b)
print(result)
