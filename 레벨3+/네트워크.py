def solution(n, computers) :
	
	
			

def main() : 
	n, computers = 3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]	# 2
	#n, computers = 3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]	# 1
	#n, computers = 3,[[1,1,1],[1,1,1],[1,1,1]]			# 1
	#n, computers = 3,[[1,1,0],[1,1,1],[0,1,1]]			# 1
	#n, computers = 3,[[1,0,0],[0,1,0],[0,0,1]]			# 3
	#n, computers = 1,[[1]]								# 1
	n, computers = 2,[[1,1],[1,1]]						# 1
	n, computers = 2,[[1,0],[0,1]]						# 2
	#n, computers = 5,[[1,1,1,1,0],[1,1,0,0,1],[1,0,1,0,1],[1,0,0,1,1],[0,1,1,1,1]]											# 1
	#n, computers = 3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
	print("solution : ", solution(n, computers)) 

main()

