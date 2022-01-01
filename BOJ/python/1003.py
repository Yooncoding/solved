"""
1003 - 피보나치 함수
https://www.acmicpc.net/problem/1003
"""

from sys import stdin

input = stdin.readline

fibo = [[1, 0], [0, 1], [1, 1]]
for i in range(3, 41):
    temp = [fibo[i - 2][0] + fibo[i - 1][0], fibo[i - 2][1] + fibo[i - 1][1]]
    fibo.append(temp)

for _ in range(int(input())):
    N = int(input())
    answer = fibo[N]
    print(answer[0], answer[1])
