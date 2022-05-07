"""
1107 - 리모컨
https://www.acmicpc.net/problem/1107
"""

n = int(input())
m = int(input())
broken = input().rsplit() if m != 0 else []

ans = abs(n - 100)

for i in range(1000000):
    for j in str(i):
        if j in broken:
            break
    else:
        ans = min(ans, abs(n - i) + len(str(i)))

print(ans)
