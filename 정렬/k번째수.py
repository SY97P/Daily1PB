# 주어진 배열을 slice 해서 정렬한 후 그 중에서 k번째로 작은 수를 꺼냄.
def solution(array, commands) :
	answer = []
	for c in commands : 
		answer.append(sorted(array[c[0]-1:c[1]])[c[2]-1])
	return answer
	

	
def main() : 
	array, commands = [1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]	# [5, 6, 3]
	print("solution : ",solution(array, commands))

main()