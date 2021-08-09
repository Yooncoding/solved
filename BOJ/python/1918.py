"""
1918 - 후위 표기식
https://www.acmicpc.net/problem/10799
"""

import sys

class Stack:
	def __init__(self):
		self.data = []
	def size(self):
		return len(self.data)
	def isEmpty(self):
		return self.size() == 0
	def push(self, item):
		self.data.append(item)
	def pop(self):
		return self.data.pop()
	def peek(self):
		return self.data[-1]
	
def solution(S):
    prec = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
    opStack = Stack()
    answer = ''
    for c in S:
        if c not in "*+-/()":
            answer += c
        if c == "(":
            opStack.push(c)
        if c == ")":
            while opStack.peek() != "(":
                answer += opStack.pop()
            opStack.pop()
        if c in "*+-/":
            if opStack.isEmpty():
                opStack.push(c)
            else:
                while prec[opStack.peek()] >= prec[c]:
                    answer += opStack.pop()
                    if opStack.isEmpty():
                        break
                opStack.push(c)
    while not opStack.isEmpty():
        answer += opStack.pop()
    return answer

data = sys.stdin.readline().rstrip()
print(solution(data))