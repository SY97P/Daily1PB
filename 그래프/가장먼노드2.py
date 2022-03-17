# 곱창난 풀이법
# def solution(n, edge) : 
# 	max_count, max_value = 0, 0
# 	# print(visited)

# 	for i in range(2, n+1) :
# 		# print(i)
# 		value = dfs(1, i, edge, n-1, 0)
# 		# print(max_value, value)
# 		if max_value < value :
# 			max_value = value
# 			max_count = 1
# 		elif max_value == value : 
# 			max_count += 1
# 		# print(max_count)

# 	# print(visited)	
# 	return max_count

# def dfs(node, wanted, edge, min_count, depth) : 
# 	if node == wanted : 
# 		return depth
# 	candi = []
# 	for e in edge : 
# 		if node in e : 
# 			candi.append(e)
# 	# print(candi)
# 	if not candi : 
# 		return -1 
# 	for c in candi : 
# 		if wanted not in c : 
# 			continue
# 		edge.remove(c)
# 		temp = dfs(c[1 if c.index(node) == 0 else 0], wanted, edge, min_count, depth + 1)
# 		edge.append(c)
# 		if temp != -1 : 
# 			if min_count > temp : 
# 				min_count = temp 

# 	return min_count

# 안 곱창난 풀이법
from collections import deque
def solution(n, edge) : 
	answer = 0
	deq = deque()
	adj = [[] for i in range(n)]
	for e in edge : 
		adj[e[0]-1].append(e[1])
		adj[e[1]-1].append(e[0])
	print(adj)
	

def main() : 
	n, edge = 6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	# 3
	n, edge = 2,[[2,1]] # 1
	n, edge = 3,[[3,1],[2,1],[2,3]]
	print("solution : ", solution(n, edge))

main()
