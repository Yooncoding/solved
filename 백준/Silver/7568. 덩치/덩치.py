from sys import stdin

input = stdin.readline

n = int(input())
group = [list(map(int, input().rsplit())) for _ in range(n)]

answer = [-1 for _ in range(n)]

for i in range(n):
    w, h = group[i]
    cnt = 0
    for j in range(n):
        if i == j:
            continue
            
        dw, dh = group[j]
        if dw > w and dh > h:
           cnt += 1
    
    answer[i] = cnt+1

print(*answer)