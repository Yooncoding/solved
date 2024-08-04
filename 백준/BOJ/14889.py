"""
14889 - 스타트와 링크
https://www.acmicpc.net/problem/14889
"""

from math import inf

INF = inf

# input
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]


def compare():
    start_team = 0
    link_team = 0
    for i in range(n):
        for j in range(n):
            if i in combination and j in combination:
                start_team += grid[i][j]
            if i not in combination and j not in combination:
                link_team += grid[i][j]

    return abs(start_team - link_team)


def backtracking(start_index, cnt):
    global ans
    if cnt == n // 2:
        s = compare()
        ans = min(s, ans)
        return

    for i in range(start_index, n):
        combination.append(i)
        backtracking(i + 1, cnt + 1)
        combination.pop()

    return


ans = INF
combination = [0]
backtracking(1, 1)
print(ans)
