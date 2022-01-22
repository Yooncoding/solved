"""
17609 - 회문
https://www.acmicpc.net/problem/17609
"""

from sys import stdin

input = stdin.readline


def pseudo_palindrome_one(s):
    left = 0
    right = len(s) - 1
    flag = False
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            if flag == True:
                return False
            if s[left + 1] == s[right]:
                left += 2
                right -= 1
                flag = True
            else:
                return False
    return True


def pseudo_palindrome_two(s):
    left = 0
    right = len(s) - 1
    flag = False
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            if flag == True:
                return False
            if s[left] == s[right - 1]:
                left += 1
                right -= 2
                flag = True
            else:
                return False
    return True


for _ in range(int(input())):
    s = input().rstrip()
    if s == s[::-1]:
        print(0)
        continue
    elif pseudo_palindrome_one(s) or pseudo_palindrome_two(s):
        print(1)
    else:
        print(2)
