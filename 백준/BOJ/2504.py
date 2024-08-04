"""
2504 - 괄호의 값
https://www.acmicpc.net/problem/2504
"""

from sys import stdin

input = stdin.readline

brackets = list(input().rstrip())  # (()[[]])
stack = []
ans = 0

for bracket in brackets:
    # opened bracket
    if bracket in "([":
        stack.append(bracket)

    # closed bracket
    else:
        if len(stack) == 0:
            ans = 0
            break

        if bracket == ")" and stack[-1] == "(":
            stack.pop()
            stack.append(2)

        elif bracket == ")" and type(stack[-1]) == int:
            temp = 0
            processing = True
            while len(stack) != 0:
                v = stack.pop()
                if type(v) == int:
                    temp += v
                elif v == "(":
                    stack.append(2*temp)
                    break
                else:
                    processing = False
                    break
            if not processing:
                ans = 0
                break

        elif bracket == "]" and stack[-1] == "[":
            stack.pop()
            stack.append(3)

        elif bracket == "]" and type(stack[-1]) == int:
            temp = 0
            processing = True
            while len(stack) != 0:
                v = stack.pop()
                if type(v) == int:
                    temp += v
                elif v == "[":
                    stack.append(3*temp)
                    break
                else:
                    processing = False
                    break
            if not processing:
                ans = 0
                break

        else:
            ans = 0
            break


for v in stack:
    if type(v) != int:
        ans = 0
        break
    else:
        ans += v

print(ans)
