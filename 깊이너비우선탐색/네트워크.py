def solution(n, computers) :
	answer = 0 
	isVisited = [False for i in range(n)]
	for i in range(n) :
		if isVisited[i] == False :
			answer += 1
			dfs(n, computers, isVisited, i)

	return answer

def dfs(n, computers, isVisited, i) :
	isVisited[i] = True
	computers[i][i] = 0
	for j in range(n) :
		if computers[i][j] == 1 and isVisited[j] == False :
			computers[i][j] = 1
			computers[j][i] = 1
			dfs(n, computers, isVisited, j)
			

def main() :
	#n, computers = 3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]		#	2
	n, computers = 3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]		#	1
#	n, computers = 5, [[1,1,0,1,0],[1,1,0,0,0],[0,0,1,0,1],[1,0,0,1,0],[0,0,1,0,1]] # 2
	#n, computers = 5, [[1,1,0,1,0],[1,1,1,0,0],[0,1,1,0,0],[1,0,0,1,1],[0,0,0,1,1]]	# 1
	#n, computers = 5, [[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]]	# 5
	print("solution : ", solution(n, computers))

main()