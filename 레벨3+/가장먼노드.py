from collections import deque
def solution(n, vertex) : 
	answer = 0
	visited = [False for i in range(n+1)]
	adj = [[] for i in range(n+1)]
	for v in vertex : 
		x, y = v
		adj[x].append(y)
		adj[y].append(x)

	print(adj)

	lst = bfs(1, visited, adj)
	return lst.count(max(lst))
		

def main() : 
	n, vertext = 6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	# 3
	print("solution : ", solution(n, vertext))

main()
