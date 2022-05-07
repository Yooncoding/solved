"""
1018 - 체스판 다시 칠하기
https://www.acmicpc.net/problem/1018
"""

from sys import stdin
input = stdin.readline

def solution(n, m, board):
    count = []
    for i in range(n - 7):
        for j in range(m - 7):
            w_first_count = 0
            b_first_count = 0
            for x in range(i, i + 8):
                for y in range(j, j + 8):
                    if (x + y) % 2 == 0:
                        if board[x][y] != "W":
                            w_first_count += 1
                        if board[x][y] != "B":
                            b_first_count += 1
                    else:
                        if board[x][y] != "W":
                            b_first_count += 1
                        if board[x][y] != "B":
                            w_first_count += 1
            count.append(min(b_first_count, w_first_count))
    return min(count)


n, m = list(map(int, input().split()))
board = []
for i in range(n):
    board.append(input().rstrip())
print(solution(n, m, board))
