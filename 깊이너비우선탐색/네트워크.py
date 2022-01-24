def solution(n, computers) :
	answer = 0
	for i in range(n) :
		for j in range(n) :
			if computers[i][j] == 1 :
				answer += 1
				findEndPoint(n, computers, i, j)
	return answer

def findEndPoint(n, computers, i, j) :
	computers[i][j] = 0
	if i == n - 1 and j == n - 1 :
		return 
	elif i == n-1 and j < n :
		if computers[i][j+1] == 0 :
			return 
		findEndPoint(n, computers, i, j+1)
	elif j == n-1 and i < n :
		if computers[i+1][j] == 0 :
			return 
		findEndPoint(n, computers, i+1, j) 
	else : 
		if computers[i][j+1] == 0 and computers[i+1][j] == 0 :
			return 
		findEndPoint(n, computers, i, j+1)
		findEndPoint(n, computers, i+1, j)

def main() :
	n, computers = 3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]		#	2
	#n, computers = 3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]		#	1
	print("solution : ", solution(n, computers))

main()