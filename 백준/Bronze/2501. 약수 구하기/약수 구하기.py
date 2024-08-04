from sys import stdin

input = stdin.readline

n, k = map(int, input().rsplit())
data = []

for i in range(1, n + 1):
    if n%i==0:
        data.append(i)

ans = data[k-1] if len(data) >= k else 0
print(ans)