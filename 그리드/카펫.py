import math

def solution(brown, yellow) :
	answer = []
	for i in range(1,int(math.sqrt(yellow))+1) :
		# i : yellow 세로 길이
		# yellow / i : yellow 가로 길이
		# i : brown 세로 길이
		# (brown - 2*i) / 2 = (yellow / i) + 2 : brown 가로 길이
		if brown/2-i == yellow/i + 2 :
			answer = [int(yellow/i+2), i+2]
		# return 할 값은 brown의 [가로, 세로]
	return answer
			

def main() :
	tc1 = [10, 2]
	tc2 = [8, 1]
	tc3 = [24, 24]
	print("solution : ", solution(tc3[0], tc3[1]))

main()

