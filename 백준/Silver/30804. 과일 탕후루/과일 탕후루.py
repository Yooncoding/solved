from sys import stdin
from itertools import combinations


input = stdin.readline

n = int(input())
# 과일 종류는 1 ~ 9 숫자로 표시
fruits = list(map(int, input().rsplit()))

# 9C2 = 9 * 8 / 2
answer = 0
for case in combinations(range(1, 10), 2):
    cnt = 0
    for fruit in fruits:
        if fruit in case:
            cnt += 1
        else:
            answer = max(answer, cnt)
            cnt = 0
            
    answer = max(answer, cnt)
    
print(answer)
        