def solution(n, computers) :
	answer = 0
	# for i in computers :
	# 	print(i) 
	for i in range(n) :
		if sum(computers[i]) == 0 :
			continue
		elif sum(computers[i]) == 1 :
			answer += 1
			computers[i][i] = 0
			continue
		computers[i][i] = 0
		for j in range(n) :
			if computers[i][j] == 1 :
				computers[i][j], computers[j][i], computers[j][j] = 0, 0, 0
				answer += findEndPoint(n, computers, j)
		if sum(computers[i]) == 0 :
			answer += 1
			# print("i : ", i, ", answer : ", answer)
	return answer 

def findEndPoint(n, computers, node) :
	# print("node : ", node)
	# for i in computers :
	# 	print(i)
	if sum(computers[node]) == 0 :
		return 0
	for k in range(n) :
		if computers[node][k] == 1: 
			computers[node][k], computers[k][node], computers[k][k] = 0, 0, 0
			return findEndPoint(n, computers, k)

def main() :
	n, computers = 3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]		#	2
	#n, computers = 3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]		#	1
	#n, computers = 5, [[1,1,0,1,0],[1,1,0,0,0],[0,0,1,0,1],[1,0,0,1,0],[0,0,1,0,1]] # 2
	n, computers = 5, [[1,1,0,1,0],[1,1,1,0,0],[0,1,1,0,0],[1,0,0,1,1],[0,0,0,1,1]]	# 1
	n, computers = 5, [[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]]	# 5
	print("solution : ", solution(n, computers))

main()