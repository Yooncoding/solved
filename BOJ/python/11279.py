"""
11279 - 최대 힙
https://www.acmicpc.net/problem/11279
"""

from sys import stdin

input = stdin.readline

def insert(item):
	heap.append(item)
	i = len(heap) - 1
	while i > 1:
		if heap[i] > heap[i // 2]:
			heap[i], heap[i // 2] = heap[i // 2], heap[i]
		else:
			break
		i //= 2

def remove():
	if len(heap) > 1:
		heap[1], heap[-1] = heap[-1], heap[1]
		item = heap.pop(-1)

		i = 1
		while True:
			left = i * 2
			right = i * 2 + 1
			smallest = i
			if left<len(heap) and heap[left] > heap[smallest]:
				smallest = left
			if right < len(heap) and heap[right] > heap[smallest]:
				smallest = right
			if smallest == i:
				break
			heap[smallest], heap[i] = heap[i], heap[smallest]
			i = smallest
	else:
		item = 0

	return item
		
heap = [None]

for _ in range(int(input())):
	x = int(input())
	if x == 0:
		print(remove())
	else:
		insert(x)


