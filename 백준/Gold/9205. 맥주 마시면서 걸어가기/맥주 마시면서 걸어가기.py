def bfs(y, x):
	global answer
	dist = abs(y-end[0]) + abs(x-end[1])
	if dist <= 1000:
		answer = "happy"
	for i, node in enumerate(nodes):
		dist = abs(y-node[0]) + abs(x-node[1])
		if dist <= 1000 and not visited_nodes[i]:
			visited_nodes[i] = True
			bfs(node[0], node[1])

for t in range(int(input())):
	n = int(input()) # 편의점 개수
	start = list(map(int, input().split())) # 집 위치
	nodes = []
	for _ in range(n):
		nodes.append(list(map(int, input().split()))) # 편의점 위치
	end = list(map(int, input().split())) # 페스티벌 위치
	
	answer = "sad"
	visited_nodes = [False for _ in range(n)]
	
	bfs(start[0], start[1])
	print(answer)
