"""
14890 - 경사로
https://www.acmicpc.net/problem/14890
"""

# input
N, L = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    flag = False
    visited = [False for _ in range(N)]
    for j in range(N-1):
        if abs(grid[i][j] - grid[i][j+1]) > 1:
            flag = True
            break

        if grid[i][j] == grid[i][j+1]:
            pass

        elif grid[i][j] > grid[i][j+1]:
            for k in range(1, L+1):
                if j + k >= N:
                    flag = True
                    break

                visited[j + k] = True
                if grid[i][j + 1] != grid[i][j + k]:
                    flag = True
                    break

        elif grid[i][j] < grid[i][j+1]:
            for k in range(L):
                if j - k < 0:
                    flag = True
                    break

                if visited[j-k]:
                    flag = True
                    break

                visited[j-k] = True
                if grid[i][j] != grid[i][j-k]:
                    flag = True
                    break

    if not flag:
        ans += 1

for j in range(N):
    flag = False
    visited = [False for _ in range(N)]
    for i in range(N-1):
        if abs(grid[i][j] - grid[i+1][j]) > 1:
            flag = True
            break

        if grid[i][j] == grid[i+1][j]:
            pass

        elif grid[i][j] > grid[i+1][j]:
            for k in range(1, L+1):
                if i + k >= N:
                    flag = True
                    break

                visited[i + k] = True
                if grid[i+1][j] != grid[i+k][j]:
                    flag = True
                    break

        elif grid[i][j] < grid[i+1][j]:
            for k in range(L):
                if i - k < 0:
                    flag = True
                    break

                if visited[i-k]:
                    flag = True
                    break

                visited[i-k] = True
                if grid[i][j] != grid[i-k][j]:
                    flag = True
                    break

    if not flag:
        ans += 1

print(ans)
