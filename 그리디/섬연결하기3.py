def solution(n, costs) : 
	answer = 0
	costs.sort(key = lambda x: x[2])
	route = set([costs[0][0]])

	while n > len(route) : 
		for i, cost in enumerate(costs) : 
			if cost[0] in route and cost[1] in route : 
				continue
			if cost[0] in route or cost[1] in route : 
				answer += cost[2]
				route.update([cost[0], cost[1]])
				cost[i] = [-1, -1, -1]

	return answer

	# answer = dfs(n, costs, route, 0)
	# return answer

# def dfs(n, costs, route, node) : 
# 	candi = []
# 	for c in costs : 
# 		if node in c and -1 not in c : 
# 			candi.append(c)
# 	print(candi)
# 	if not candi : 
# 		return 0
# 	for c in candi : 
# 		next_node = c[0] if c[0] != node else c[1]
# 		print("next_node : ", next_node)
# 		if next_node not in route : 
# 			costs[costs.index(c)] = [-1,-1,-1]
# 			route.add(next_node)
# 			return c[2] + dfs(n, costs, route, next_node)
	
			

def main() : 
	n, costs = 4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]	# 4
	print("solution : ", solution(n, costs))

main()
