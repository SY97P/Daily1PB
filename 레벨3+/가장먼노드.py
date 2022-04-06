from collections import deque
def solution(n, vertex) : 
	answer = 0
	visited = [-1 for i in range(n)]
	
	adj = [[] for i in range(n+1)]
	for v in vertex : 
		x, y = v
		adj[x].append(y)
		adj[y].append(x)

	# print(adj)

	bfs(1, visited, adj)

	return visited.count(max(visited))

def bfs(node, visited, adj) : 
	count = 1
	queue = deque([[node, count]])

	while queue : 
		curr = queue.popleft()
		# print("curr  : ", curr)
		# print("queue : ", queue)
		n, c = curr
		if visited[n-1] == -1 : 
			visited[n-1] = c
			# print("visited : ", visited[n-1])
			for v in adj[n] : 
				queue.append([v, c+1])
	
		

def main() : 
	n, vertext = 6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	# 3
	print("solution : ", solution(n, vertext))

main()
