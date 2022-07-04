"""
14891 - 톱니바퀴
https://www.acmicpc.net/problem/14891
"""


def right_rotate(i):
    temp = gears[i][-1]
    for j in range(7, 0, -1):
        gears[i][j] = gears[i][j-1]
    gears[i][0] = temp
    return


def left_rotate(i):
    temp = gears[i][0]
    for j in range(7):
        gears[i][j] = gears[i][j+1]
    gears[i][-1] = temp
    return


def simulate(n, dir_num):
    rotate_status = [0 for _ in range(4)]  # 0은 유지, 1은 시계 방향, -1은 반시계 방향
    rotate_status[n] = dir_num
    temp_n, temp_dir_num = n, dir_num
    left, right = n-1, n+1

    while left > -1:
        if gears[n][6] == gears[left][2]:
            break
        dir_num *= -1
        rotate_status[left] = dir_num
        n -= 1
        left -= 1

    n, dir_num = temp_n, temp_dir_num
    while right < 4:
        if gears[n][2] == gears[right][6]:
            break
        dir_num *= -1
        rotate_status[right] = dir_num
        n += 1
        right += 1

    for i in range(4):
        if rotate_status[i] == 1:
            right_rotate(i)
        if rotate_status[i] == -1:
            left_rotate(i)

    return


# input
gears = [list(map(int, input())) for _ in range(4)]
k = int(input())
for _ in range(k):
    start, start_dir_num = map(int, input().split())
    simulate(start-1, start_dir_num)

ans = 0
for i in range(4):
    if gears[i][0] == 1:
        ans += (2 ** i)
print(ans)
