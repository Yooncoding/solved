"""
15684 - 사다리 조작
https://www.acmicpc.net/problem/15684
"""

# input
n, m, h = map(int, input().split())
bridge = [[False for _ in range(n)] for _ in range(h)]
for _ in range(m):
    a, b = map(int, input().split())
    bridge[a-1][b-1] = True


def check():
    for start in range(n):
        j = start
        for i in range(h):
            if bridge[i][j]:
                j += 1
            elif j > 0 and bridge[i][j-1]:
                j -= 1
        if start != j:
            return False

    return True


def btk(cnt, start_row, start_col):
    global ans
    if cnt > 3 or ans <= cnt:
        return

    if check():
        ans = min(ans, cnt)

    for i in range(start_row, h):
        for j in range(start_col, n-1):
            if not bridge[i][j] and not bridge[i][j+1]:
                bridge[i][j] = True
                btk(cnt+1, i, j+2)
                bridge[i][j] = False
        start_col = 0

    return


ans = 4
btk(0, 0, 0)
ans = -1 if ans == 4 else ans
print(ans)
