def solution(length, weight, trucks) :
	answer = 0
	queue = [0 for i in range(length)]

	# print(len(trucks) * 5 + 1)

	trucks.reverse()
	while trucks : 
		truck = trucks.pop()
		# print(truck)
		if sum(queue) == 0 : 
			queue = queue[1:] + [truck]
			answer += 1
			print("answer : ", answer, "queue : ", queue)
			continue
		if sum(queue) + truck <= weight :
			queue = queue[1:] + [truck]
		while sum(queue) + truck > weight : 
			queue = queue[1:] + [0]
			answer += 1
			print("answer : ", answer, "queue : ", queue)
		# queue = queue[1:] + [truck]
		# print("answer1 : ", answer, "queue : ", queue)
	while sum(queue) != 0 :
		answer += 1
		queue = queue[1:] + [0]
	return answer


def main() : 
	length, weight, trucks = 2, 10, [7,4,5,6]	#8
	#length, weight, trucks = 100, 100, [10]	#101
	#length, weight, trucks = 100, 100, [10,10,10,10,10,10,10,10,10,10]	#110
	#length, weight, trucks = 5, 5, [5, 5, 5, 5, 5, 5] # 31
	print("solution : ", solution(length, weight, trucks))

main()