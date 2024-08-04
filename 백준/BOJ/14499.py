"""
14499 - 주사위 굴리기
https://www.acmicpc.net/problem/14499
"""


# input
n, m, r, c, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()))

dr, dc = [0, 0, 0, -1, 1], [0, 1, -1, 0, 0]  # 인덱스 1 ~ 4 만 사용

dice_value = [0 for _ in range(7)]  # 인덱스 1 ~ 6 만 사용
dice_index = [
    [0, 2, 0],
    [4, 1, 3],
    [0, 5, 0],
    [0, 6, 0]
]  # 주사위 인덱스


def in_range(r, c):
    return 0 <= r < n and 0 <= c < m


ans = []
for command in commands:
    nr, nc = r + dr[command], c + dc[command]
    if not in_range(nr, nc):
        continue

    if command == 1:
        temp = dice_index[1][2]
        for i in range(2, 0, -1):
            dice_index[1][i] = dice_index[1][i-1]
        dice_index[1][0] = dice_index[3][1]
        dice_index[3][1] = temp

    elif command == 2:
        temp = dice_index[1][0]
        for i in range(0, 2):
            dice_index[1][i] = dice_index[1][i+1]
        dice_index[1][2] = dice_index[3][1]
        dice_index[3][1] = temp

    elif command == 3:
        temp = dice_index[0][1]
        for i in range(0, 3):
            dice_index[i][1] = dice_index[i+1][1]
        dice_index[3][1] = temp

    elif command == 4:
        temp = dice_index[3][1]
        for i in range(3, 0, -1):
            dice_index[i][1] = dice_index[i-1][1]
        dice_index[0][1] = temp

    top_index = dice_index[1][1]
    bottom_index = dice_index[3][1]
    ans.append(dice_value[top_index])

    if grid[nr][nc] == 0:
        grid[nr][nc] = dice_value[bottom_index]
    else:
        dice_value[bottom_index] = grid[nr][nc]
        grid[nr][nc] = 0

    r, c = nr, nc

for i in range(len(ans)):
    print(ans[i])
