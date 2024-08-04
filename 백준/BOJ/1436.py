"""
1436 - 영화감독 숌
https://www.acmicpc.net/problem/1436
"""

import sys

n = int(sys.stdin.readline())
num = 666 
count = 0

while True:
    if "666" in str(num): 
        count += 1 
    if count == n: 
        print(num) 
        break
    num += 1