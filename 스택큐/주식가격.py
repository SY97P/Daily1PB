def solution(prices) : 
	answer = []

	for i, p in enumerate(prices): 
		# print("i, p : ", i, p)
		count = 0
		if len(prices) == 1 :
			answer.append(0)
			break 
		for t in prices[i+1:] :
			count += 1
			if t < p : 
				break 
		# print("count : ", count)
		answer.append(count)
		# print(answer)

	return answer

def main() : 
	prices = [1, 2, 3, 2, 3]	# [4, 3, 1, 1, 0]
	prices = [5, 2, 3, 1, 4]	# [1, 2, 1, 1, 0]
	print("solution : ", solution(prices))

main()