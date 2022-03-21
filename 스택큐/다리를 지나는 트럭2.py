def solution(length, weight, trucks) :
	answer = 0 
	bridge = [0] * length

	while True : 
		answer += 1
		bridge.pop(0)

		if not trucks : 
			break
		if sum(bridge) + trucks[0] <= weight : 
			bridge.append(trucks.pop(0))
		else : 
			bridge.append(0)

	return answer

def main() : 
	length, weight, trucks = 2, 10, [7,4,5,6]	#8
	length, weight, trucks = 100, 100, [10]	#101
	length, weight, trucks = 100, 100, [10,10,10,10,10,10,10,10,10,10]	#110
	length, weight, trucks = 5, 5, [5, 5, 5, 5, 5, 5] # 31
	print("solution : ", solution(length, weight, trucks))

main()