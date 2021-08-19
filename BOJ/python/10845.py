"""
10845 - 큐
https://www.acmicpc.net/problem/10845
"""

import sys

class Queue:
	def __init__(self):
		self.data = []
	
	def size(self):
		return len(self.data)
		
	def isEmpty(self):
		return 1 if self.size() == 0 else 0

	def enqueue(self, item):
		self.data.append(item)
	
	def dequeue(self):
		return self.data.pop(0) if self.isEmpty() == 0 else -1
	
	def front(self):
		return self.data[0] if self.isEmpty() == 0 else -1
	
	def back(self):
		return self.data[-1] if self.isEmpty() == 0 else -1

q = Queue()
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
	order = sys.stdin.readline().rsplit()
	if order[0] == "push":
		q.enqueue(int(order[1]))
	elif order[0] == "pop":
		print(q.dequeue())
	elif order[0] == "front":
		print(q.front())
	elif order[0] == "back":
		print(q.back())
	elif order[0] == "empty":
		print(q.isEmpty())
	elif order[0] == "size":
		print(q.size())