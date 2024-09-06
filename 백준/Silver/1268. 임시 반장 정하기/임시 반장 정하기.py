from sys import stdin

input = stdin.readline

n = int(input())
class_info = [list(map(int, input().rsplit())) for _ in range(n)]

meet_info = [[False for _ in range(n)] for _ in range(n)]

for i in range(5):
  for j in range(n):
    for k in range(j, n):
      if class_info[j][i] == class_info[k][i]:
        meet_info[j][k] = 1
        meet_info[k][j] = 1

max_cnt = 0
max_student = 0
for cur_student in range(n):
  cur_cnt = sum(meet_info[cur_student])
  if max_cnt >= cur_cnt:
    continue

  else:
    max_cnt = cur_cnt
    max_student = cur_student

print(max_student+1)
  
    