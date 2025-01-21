from sys import stdin

input = stdin.readline

# 10 11 12
# 4

def cal(a, b, c):
    if b == 1:
        return a%c
    else:
        k = cal(a, b//2, c)
        if b % 2 == 0:
            return (k*k)%c
        else:
            return (k*k*a)%c

a, b, c = map (int, input().rsplit())
ans = cal(a, b, c)
print(ans)