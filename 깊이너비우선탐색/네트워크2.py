def solution(n, computers) :
	network = set()
	answer = 0 
	for i in range(n) : 
		if i not in network : 
			answer += 1
			dfs(n, computers, network, i)
	return answer

def dfs(n, computers, network, node) :
	network.add(node)
	for i, c in enumerate(computers[node]) : 
		if c == 1 and i != node : 
			computers[node][i] = 0
			dfs(n, computers, network, i)
	

def main() : 
	n, computers = 3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]	# 2
	#n, computers = 3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]	# 1
	print("solution : ", solution(n, computers))

main()
