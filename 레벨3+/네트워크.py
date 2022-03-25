def solution(n, computers) :
	answer = 1
	adj = [[] for i in range(n)]
	route = set()

	for i, info in enumerate(computers): 
		for j, conn in enumerate(info) : 
			if i != j and conn == 1 :
				adj[i].append(j)

	# print(adj)

	while len(route) < n : 
		for i in range(n) :
			if i in route : 
				continue
			route.add(i)
			if not adj[i] : 
				answer += 1
				continue
			for a in adj[i] : 
				route.add(a)

	return answer if answer <= n else n

def main() : 
	n, computers = 3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]	# 2
	n, computers = 3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]	# 1
	n, computers = 3,[[1,1,1],[1,1,1],[1,1,1]]			# 1
	n, computers = 3,[[1,1,0],[1,1,1],[0,1,1]]			# 1
	n, computers = 3,[[1,0,0],[0,1,0],[0,0,1]]			# 3
	n, computers = 1,[[1]]								# 1
	n, computers = 2,[[1,1],[1,1]]						# 1
	n, computers = 2,[[1,0],[0,1]]						# 2
	n, computers = 5,[[1,1,1,1,0],[1,1,0,0,1],[1,0,1,0,1],[1,0,0,1,1],[0,1,1,1,1]]											# 1
	print("solution : ", solution(n, computers)) 

main()

