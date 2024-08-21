"""
https://www.acmicpc.net/problem/1043
"""
from collections import defaultdict, deque

n, m = map(int, input().split())
truth_info = list(map(int, input().split()))
tn, tp = truth_info[0], truth_info[1:]
people = [False for _ in range(n+1)]
visited = [False for _ in range(n+1)]
for i in range(len(tp)):
	people[tp[i]] = True




party = {}
graph = defaultdict(set)
for i in range(m):
	party_info = list(map(int, input().split()))
	pn, pp = party_info[0], party_info[1:]	
	party[i] = pp
	for j in range(pn):
		for k in range(pn):
			graph[pp[j]].add(pp[k])
			

# print(people)
# print(party)
# print(graph)

def dfs(v):
	q = deque()
	q.append(v)
	visited[v] = True
	while len(q):
		v = q.popleft()
		for t in graph[v]:
			if visited[t]:
				continue
			q.append(t)
			visited[t] = True
			people[t] = True


for i in range(1, n+1):
	if people[i]:
		dfs(i)

# print(people)

answer = 0
for i in range(m):
	answer += 1
	for n in party[i]:
		if people[n]:
			answer -= 1
			break
	
print(answer)


	
	

