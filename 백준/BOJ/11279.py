"""
11279 - 최대 힙
https://www.acmicpc.net/problem/11279
"""


def insert(item):
    heap.append(item)
    i = len(heap) - 1
    while i > 1:
        if heap[i] > heap[i // 2]:
            heap[i], heap[i // 2] = heap[i // 2], heap[i]
        else:
            break
        i //= 2
    return


def remove():
    if len(heap) <= 1:
        return 0

    heap[1], heap[-1] = heap[-1], heap[1]
    item = heap.pop()

    i = 1
    while True:
        left = i * 2
        right = i * 2 + 1
        biggest = i

        if left < len(heap) and heap[biggest] < heap[left]:
            biggest = left
        if right < len(heap) and heap[biggest] < heap[right]:
            biggest = right
        if biggest == i:
            break
        heap[i], heap[biggest] = heap[biggest], heap[i]
        i = biggest

    return item


heap = [None]

for N in range(int(input())):
    x = int(input())
    if x == 0:
        print(remove())
    else:
        insert(x)
