"""
14501 - 퇴사
https://www.acmicpc.net/problem/14501
"""

# input
n = int(input())
schedules = [0] + [list(map(int, input().split())) for _ in range(n)]

ans = 0


def backtracking(d, s):
    global ans
    if d == n+1:
        ans = max(ans, s)
        return

    if d > n+1:
        return

    backtracking(d+1, s)
    backtracking(d+schedules[d][0], s+schedules[d][1])


backtracking(1, 0)
print(ans)
