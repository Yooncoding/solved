"""
1541 - 잃어버린 괄호
https://www.acmicpc.net/problem/1541
"""

expr = input().rstrip()
tokens = expr.split("-")

ans = 0
flag = False
for token in tokens:
    if token == "":
        pass
    elif token.isdigit():
        ans = ans - int(token) if flag else ans + int(token)
    else:
        temp = sum(map(int, token.split("+")))
        ans = ans - temp if flag else ans + temp
    flag = True

print(ans)
