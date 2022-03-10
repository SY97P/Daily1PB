def solution(triangle) : 
	answer = 0
	triangle.reverse()
	# for t in triangle : 
	# 	print(t)
	for i in range(1, len(triangle)) : 
		for j, t in enumerate(triangle[i]) : 
			triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j+1])
	# for t in triangle : 
	# 	print(t)
	return triangle[len(triangle)-1][0]
			
		

def main() : 
	triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]	# 30
	print("solution : ", solution(triangle))

main()
