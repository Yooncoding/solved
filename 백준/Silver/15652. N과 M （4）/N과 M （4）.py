from sys import stdin

input = stdin.readline

n, m = map(int, input().rsplit())
 
s = []
def dfs(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(start, n+1):
        s.append(i)
        dfs(i)
        s.pop()
    
dfs(1)