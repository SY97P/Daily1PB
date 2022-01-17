from itertools import combinations

def solution(number, k) :
	maxValue = -1
	# lst = list(map(''.join, combinations(number, len(number)-k)))
	# for item in lst : 
	# 	if (maxValue < int(item)) :
	# 		maxValue = int(item)
	# return str(maxValue)
	return max(list(map(''.join, combinations(number, len(number)-k))))

def main() :
	number, k = "1924", 2			# 94
	#number, k = "1231234", 3  		# 3234
	number, k = "4177252841", 4 	# 775841
	print("solution : ", solution(number, k))

main()