from sys import stdin

input = stdin.readline

n, m, b = list(map(int, input().rsplit()))
ground = [list(map(int, input().rsplit())) for _ in range(n)]

min_time = int(1e9)
max_height = 0

for height in range(257):
    time_cost = 0
    cur_block = b

    for r in range(n):
        for c in range(m):
            if ground[r][c] > height:
                time_cost += 2 * (ground[r][c] - height)
                cur_block += ground[r][c] - height
            else:
                time_cost += height - ground[r][c]
                cur_block -= height - ground[r][c]

    if cur_block < 0:
        continue

    if min_time >= time_cost:
        min_time = time_cost
        max_height = height

print(min_time, max_height)
