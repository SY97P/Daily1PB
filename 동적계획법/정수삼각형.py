def solution(triangle) :
	answer = 0
	maxlst = triangle[len(triangle)-1]
	for rowIndex, row in enumerate(reversed(triangle)) :
		#print(rowIndex, row)
		if rowIndex == 0 :
			continue
		lst = []
		for i, num in enumerate(row) : 
			lst.append(max(num+maxlst[i], num+maxlst[i+1]))
		#print(lst)
		maxlst = lst
	return maxlst[0]

def main() :
	triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]	# 30
	print("solution : ", solution(triangle))

main()