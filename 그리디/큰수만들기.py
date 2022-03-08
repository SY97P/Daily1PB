from itertools import combinations

def solution(number, k) :
	answer = []
	index = -1
	for num in number :
		if not answer :
			answer.append(num)
			continue
		if k > 0 :
			while answer[-1] < num :
				answer.pop()
				k -= 1
				if not answer or k <= 0 :
					break
		answer.append(num)
	answer = answer[:-k] if k > 0  else answer
	return ''.join(answer)

def main() :
	number, k = "1924", 2			# 94
	#number, k = "1231234", 3  		# 3234
	number, k = "4177252841", 4 	# 775841
	print("solution : ", solution(number, k))

main()