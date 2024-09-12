from sys import stdin
from collections import defaultdict

input = stdin.readline

n = int(input())
m = int(input())

routes = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().rsplit())
    routes[a].append([b, c])

origin, dest = map(int, input().rsplit())

def get_next_city():
    min_value = 1e9
    min_index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            min_index = i

    return min_index

visited = [False for _ in range(n+1)]
distance = [1e9 for _ in range(n+1)]

def dijkstra(start):
    distance[start] = 0

    for i in range(n):
        city = get_next_city()

        if city == 0:
            break

        visited[city] = True
        for ncity, cost in routes[city]:
            distance[ncity] = min(cost + distance[city], distance[ncity])

dijkstra(origin)
print(distance[dest])