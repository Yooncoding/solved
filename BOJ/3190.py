"""
3190 - 뱀
https://www.acmicpc.net/problem/3190
"""

# input
n = int(input())
k = int(input())
grid = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(k):
    r, c = map(int, input().split())
    grid[r-1][c-1] = 2

times = []
timeline = dict()
m = int(input())
for _ in range(m):
    time, direction = input().split()
    time = int(time)
    times.append(time)
    timeline[time] = direction
# ex) times = [3, 15, 17], timeline = {3: 'D', 15: 'L', 17: 'D'}

dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]  # 우 하 좌 상


def in_range(r, c):
    return 0 <= r < n and 0 <= c < n


def go(point):
    hr, hc = point  # 머리 좌표
    tr, tc = point  # 꼬리 좌표
    hdir_num, tdir_num = 0, 0  # 머리의 방향, 꼬리의 방향
    hpointer, tpointer = 0, 0  # 머리와 꼬리의 각 times index를 가리킴
    hcnt, tcnt = 0, 0
    while True:
        nhr, nhc = hr + dr[hdir_num], hc + dc[hdir_num]
        ntr, ntc = tr + dr[tdir_num], tc + dc[tdir_num]

        # 다음 이동할 머리가 벽일 때
        if not in_range(nhr, nhc):
            return hcnt + 1

        # 다음 이동할 머리가 뱀의 몸통일 때
        if grid[nhr][nhc] == 1:
            return hcnt + 1

        # 다음 이동할 머리가 사과일 때
        # 꼬리는 자리 그대로 있기 때문에 머리만 위치 변경
        if grid[nhr][nhc] == 2:
            grid[nhr][nhc] = 1
            hr, hc = nhr, nhc
            hcnt += 1

        # 다음 이동할 머리가 빈 공간일 때
        # 꼬리도 같이 이동하기 때문에 머리와 꼬리 위치 변경
        else:
            grid[nhr][nhc] = 1
            grid[tr][tc] = 0
            hr, hc = nhr, nhc
            tr, tc = ntr, ntc
            hcnt += 1
            tcnt += 1

        # 머리의 방향 회전
        if hpointer < len(times) and times[hpointer] == hcnt:
            if timeline[times[hpointer]] == 'D':
                hdir_num = (hdir_num + 1) % 4
            else:
                hdir_num = (hdir_num + 3) % 4
            hpointer += 1

        # 꼬리의 방향 회전
        if tpointer < len(times) and times[tpointer] == tcnt:
            if timeline[times[tpointer]] == 'D':
                tdir_num = (tdir_num + 1) % 4
            else:
                tdir_num = (tdir_num + 3) % 4
            tpointer += 1


start_point = (0, 0)
grid[0][0] = 1
ans = go(start_point)
print(ans)
