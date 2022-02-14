def solution(prices) : 
	length = len(prices)
	answer = [0] * length
	for i in range(length) : 
		for j in range(i+1, length) : 
			answer[i] += 1
			if prices[j] < prices[i] :
				break
	return answer


def main() : 
	prices = [1,2,3,2,3]	# [4,3,1,1,0]
	prices = [3,4,2,3,1,2]	# [2,1,2,1,1,0]
	print("solution : ", solution(prices))

main() 