r = set()
for x in range(1,10000):
  sum = x
  for c in str(x):
    sum += int(c)
  r.add(sum)
for y in range(1,10000):
  if y not in r:
    print(y)