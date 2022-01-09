"""
1541 - 잃어버린 괄호
https://www.acmicpc.net/problem/1541
"""

from sys import stdin

input = stdin.readline

expr = input().rstrip()
tokens = []
val = 0

for c in expr:
    if c in "0123456789":
        val = val * 10 + int(c)
    else:
        tokens.append(val)
        val = 0
        tokens.append(c)
tokens.append(val)

nums = []
minus_flag = False
temp = 0
for token in tokens:
    if token == "-":
        nums.append(-temp)
        temp = 0
        minus_flag = True
    elif token == "+":
        continue
    else:
        if minus_flag == True:
            temp += token
        else:
            nums.append(token)
nums.append(-temp)

print(sum(nums))
