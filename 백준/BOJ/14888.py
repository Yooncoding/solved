"""
14888 - 연산자 끼워넣기
https://www.acmicpc.net/problem/14888
"""

from math import inf
INF = inf

# input
n = int(input())
a = list(map(int, input().split()))
operation_cnt = list(map(int, input().split()))  # +, -, *, //


def backtracking(cnt, s):
    global max_ans, min_ans
    if cnt == n-1:
        max_ans = max(s, max_ans)
        min_ans = min(s, min_ans)
        return

    for i in range(4):
        if operation_cnt[i] == 0:
            continue
        operation_cnt[i] -= 1
        if i == 0:
            backtracking(cnt+1, s + a[cnt+1])
        elif i == 1:
            backtracking(cnt+1, s - a[cnt+1])
        elif i == 2:
            backtracking(cnt+1, s * a[cnt+1])
        else:
            if s * a[cnt+1] > 0:
                backtracking(cnt+1, s // a[cnt+1])
            else:
                backtracking(cnt+1, (abs(s) // abs(a[cnt+1])) * (-1))
        operation_cnt[i] += 1

    return


max_ans, min_ans = -INF, INF
backtracking(0, a[0])
print(max_ans)
print(min_ans)
