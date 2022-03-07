import math
def solution(brown, yellow) : 
	mid = int(math.sqrt(yellow))
	for i in range(mid, 0, -1) : 
		if brown / 2 - i == yellow / i + 2 :
			return [int(yellow/i+2),i+2]
	return []

def main() : 
	brown, yellow = 10 ,2	# [4, 3]
	#brown, yellow = 8, 1	# [3, 3]
	#brown, yellow = 24, 24	# [8, 6]
	print("solution : ", solution(brown, yellow))

main()
