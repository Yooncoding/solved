"""
13458 - 시험 감독
https://www.acmicpc.net/problem/13458
"""

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())


ans = 0
for i in range(n):
    cnt = 1  # 총 감독관 1명
    a[i] = a[i] - b if a[i] > 0 else 0  # 음수일 때, 0으로 처리

    if a[i] % c == 0:
        cnt += (a[i] // c)
    else:
        cnt += (a[i] // c) + 1

    ans += cnt

print(ans)
