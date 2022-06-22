"""
13460 - 구슬 탈출 2
https://www.acmicpc.net/problem/13460
"""

from collections import deque

n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]


def left_move(red, blue):
    rr, rc = red
    br, bc = blue

    if rr == br and rc > bc:
        for i in range(bc, -1, -1):
            if grid[br][i] == 'O':
                blue = False
                break
            elif grid[br][i] == '#' or ((br, i) == red):
                blue = (br, i+1)
                break
            else:
                blue = (br, 1)

        for i in range(rc, -1, -1):
            if grid[rr][i] == 'O':
                red = False
                break
            elif grid[rr][i] == '#' or ((rr, i) == blue):
                red = (rr, i+1)
                break
            else:
                red = (rr, 1)
    else:
        for i in range(rc, -1, -1):
            if grid[rr][i] == 'O':
                red = False
                break
            elif grid[rr][i] == '#' or ((rr, i) == blue):
                red = (rr, i+1)
                break
            else:
                red = (rr, 1)

        for i in range(bc, -1, -1):
            if grid[br][i] == 'O':
                blue = False
                break
            elif grid[br][i] == '#' or ((br, i) == red):
                blue = (br, i+1)
                break
            else:
                blue = (br, 1)

    return red, blue


def right_move(red, blue):
    rr, rc = red
    br, bc = blue

    if rr == br and bc > rc:
        for i in range(bc, m):
            if grid[br][i] == 'O':
                blue = False
                break
            elif grid[br][i] == '#' or ((br, i) == red):
                blue = (br, i-1)
                break
            else:
                blue = (br, m-2)

        for i in range(rc, m):
            if grid[rr][i] == 'O':
                red = False
                break
            elif grid[rr][i] == '#' or ((rr, i) == blue):
                red = (rr, i-1)
                break
            else:
                red = (rr, m-2)

    else:
        for i in range(rc, m):
            if grid[rr][i] == 'O':
                red = False
                break
            elif grid[rr][i] == '#' or ((rr, i) == blue):
                red = (rr, i-1)
                break
            else:
                red = (rr, m-2)

        for i in range(bc, m):
            if grid[br][i] == 'O':
                blue = False
                break
            elif grid[br][i] == '#' or ((br, i) == red):
                blue = (br, i-1)
                break
            else:
                blue = (br, m-2)

    return red, blue


def up_move(red, blue):
    rr, rc = red
    br, bc = blue

    if rc == bc and rr > br:
        for i in range(br, -1, -1):
            if grid[i][bc] == 'O':
                blue = False
                break
            elif grid[i][bc] == '#' or ((i, br) == red):
                blue = (i+1, bc)
                break
            else:
                blue = (1, bc)

        for i in range(rr, -1, -1):
            if grid[i][rc] == 'O':
                red = False
                break
            elif grid[i][rc] == '#' or ((i, rc) == blue):
                red = (i+1, rc)
                break
            else:
                red = (1, rc)

    else:
        for i in range(rr, -1, -1):
            if grid[i][rc] == 'O':
                red = False
                break
            elif grid[i][rc] == '#' or (i, rc) == blue:
                red = (i+1, rc)
                break
            else:
                red = (1, rc)

        for i in range(br, -1, -1):
            if grid[i][bc] == 'O':
                blue = False
                break
            elif grid[i][bc] == '#' or ((i, bc) == red):
                blue = (i+1, bc)
                break
            else:
                blue = (1, bc)

    return red, blue


def down_move(red, blue):
    rr, rc = red
    br, bc = blue

    if rc == bc and br > rr:
        for i in range(br, n):
            if grid[i][bc] == 'O':
                blue = False
                break
            elif grid[i][bc] == '#' or ((i, bc) == red):
                blue = (i-1, bc)
                break
            else:
                blue = (1, bc)

        for i in range(rr, n):
            if grid[i][rc] == 'O':
                red = False
                break
            elif grid[i][rc] == '#' or ((i, rc) == blue):
                red = (i-1, rc)
                break
            else:
                red = (1, rc)

    else:
        for i in range(rr, n):
            if grid[i][rc] == 'O':
                red = False
                break
            elif grid[i][rc] == '#' or ((i, rc) == blue):
                red = (i-1, rc)
                break
            else:
                red = (1, rc)

        for i in range(br, n):
            if grid[i][bc] == 'O':
                blue = False
                break
            elif grid[i][bc] == '#' or ((i, bc) == red):
                blue = (i-1, bc)
                break
            else:
                blue = (1, bc)

    return red, blue


def bfs(red, blue):
    q = deque()
    q.append([red, blue, 0])
    visited = []
    visited.append((red, blue))
    while len(q):
        red, blue, cnt = q.popleft()

        if cnt == 10:
            continue

        left_red, left_blue = left_move(red, blue)
        right_red, right_blue = right_move(red, blue)
        up_red, up_blue = up_move(red, blue)
        down_red, down_blue = down_move(red, blue)

        if left_blue:
            if not left_red:
                return cnt + 1

            if (left_red, left_blue) not in visited:
                q.append([left_red, left_blue, cnt+1])
                visited.append((left_red, left_blue))

        if right_blue:
            if not right_red:
                return cnt + 1

            if (right_red, right_blue) not in visited:
                q.append([right_red, right_blue, cnt+1])
                visited.append((right_red, right_blue))

        if up_blue:
            if not up_red:
                return cnt + 1

            if (up_red, up_blue) not in visited:
                q.append([up_red, up_blue, cnt+1])
                visited.append((up_red, up_blue))

        if down_blue:
            if not down_red:
                return cnt + 1
            if (down_red, down_blue) not in visited:
                q.append([down_red, down_blue, cnt+1])
                visited.append((down_red, down_blue))

    return -1


for i in range(n):
    for j in range(m):
        if grid[i][j] == 'R':
            red_marble = (i, j)
        if grid[i][j] == 'B':
            blue_marble = (i, j)

ans = bfs(red_marble, blue_marble)
print(ans)
