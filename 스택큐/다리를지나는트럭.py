def solution(length, weight, trucks) :
	answer = 0
	queue = [0 for i in range(length)]

	while True : 
		queue.pop(0)
		answer += 1
		if not trucks :
			# print("answer : ", answer, "trucks : ", trucks)
			break
		if sum(queue) + trucks[0] <= weight : 
			queue.append(trucks.pop(0))
			# print("answer : ", answer, "queue : ", queue)
		else : 
			queue.append(0)
			# print("answer : ", answer, "queue : ", queue)

	return answer + length - 1


def main() : 
	length, weight, trucks = 2, 10, [7,4,5,6]	#8
	length, weight, trucks = 100, 100, [10]	#101
	length, weight, trucks = 100, 100, [10,10,10,10,10,10,10,10,10,10]	#110
	length, weight, trucks = 5, 5, [5, 5, 5, 5, 5, 5] # 31
	print("solution : ", solution(length, weight, trucks))

main()