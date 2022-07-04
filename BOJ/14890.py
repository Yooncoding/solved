"""
14890 - 경사로
https://www.acmicpc.net/problem/14890
"""

# input
N, L = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]


def check(route):
    made = [False for _ in range(N)]
    for i in range(N-1):
        if abs(route[i] - route[i+1]) > 1:
            return False

        elif route[i] > route[i+1]:
            for j in range(1, L+1):
                if i + j >= N or route[i+1] != route[i+j]:
                    return False
                made[i+j] = True

        elif route[i] < route[i+1]:
            for j in range(L):
                if i - j < 0 or made[i-j] or route[i] != route[i-j]:
                    return False
                made[i-j] = True

    return True


ans = 0
for i in range(N):
    check_route = [grid[i][j] for j in range(N)]
    if check(check_route):
        ans += 1

for j in range(N):
    check_route = [grid[i][j] for i in range(N)]
    if check(check_route):
        ans += 1

print(ans)
