def solution(triangle) : 
	answer = 0 
	triangle.reverse()

	for k in range(1, len(triangle)) : 
		lst = [] 
		step = triangle[k]
		for i,s in enumerate(step) : 
			lst.append(max(triangle[k-1][i], triangle[k-1][i+1])+s)
		# print(lst)
		triangle[k] = lst

	return triangle[len(triangle)-1][0]
	

def main() : 
	triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]	# 30
	print("solution : ", solution(triangle))

main()

