import sys
n = int(sys.stdin.readline().rstrip())
numbers = [0] * 10001
for i in range(0,n):
  number = int(sys.stdin.readline().rstrip())
  numbers[number] = numbers[number] + 1
for i in range(0,10001):
  if numbers[i] != 0:
    for j in range(numbers[i]):
      print(i)