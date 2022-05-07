"""
10828 - 스택
https://www.acmicpc.net/problem/10828
"""

import sys


class Stack:
    def __init__(self):
        self.a = []

    def push(self, x):
        self.a.append(x)

    def pop(self):
        return self.a.pop() if self.empty() == 0 else -1

    def size(self):
        return len(self.a)

    def empty(self):
        return 1 if self.size() == 0 else 0

    def top(self):
        return self.a[-1] if self.empty() == 0 else -1


stack = Stack()

n = int(sys.stdin.readline())

for _ in range(n):
    data = sys.stdin.readline().split()

    if data[0] == 'push':
        stack.push(int(data[1]))
    elif data[0] == 'pop':
        print(stack.pop())
    elif data[0] == 'size':
        print(stack.size())
    elif data[0] == 'empty':
        print(stack.empty())
    elif data[0] == 'top':
        print(stack.top())
