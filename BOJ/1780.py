"""
1780 - 종이의 개수
https://www.acmicpc.net/problem/1780
"""


def cut(size, y=0, x=0):
    for i in range(size):
        for j in range(size):
            if nums[y][x] != nums[y + i][x + j]:
                div = size // 3
                cut(div, y, x)
                cut(div, y + div, x)
                cut(div, y + div * 2, x)
                cut(div, y, x + div)
                cut(div, y + div, x + div)
                cut(div, y + div * 2, x + div)
                cut(div, y, x + div * 2)
                cut(div, y + div, x + div * 2)
                cut(div, y + div * 2, x + div * 2)
                return
    ans[nums[y][x] + 1] += 1
    return


n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]
ans = [0, 0, 0]

cut(n)
print(*ans, sep="\n")
