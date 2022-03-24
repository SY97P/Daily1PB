import heapq
def solution(operations) : 
	answer = [0,0] 	# 마지막에 큐가 비었으면 이거 return, 아니면 [max, min] return 

	queue = []
	heapq.heapify(queue)

	for o in operations : 
		command, value = o.split(" ")
		# print(command, value)

		if command == "D" :
			if queue : 
				if value == "1" : # 최대값 삭제
					queue.remove(max(queue))
				else : 			# 최소값 삭제
					heapq.heappop(queue)
		else : 
			value = int(value)
			heapq.heappush(queue, value)

		# for q in queue : 
		# 	print(q, end = " ")
		# print()

	if queue : 
		answer = [int(max(queue)), int(min(queue))]
	return answer
	

def main() : 
	operations = ["I 16","D 1"]					# [0,0]
	#operations = ["I 7","I 5","I -5","D -1"]	# [7,5]
	operations = ["D 1"]						# [0,0]
	operations = ["I 7", "I 7", "D 1"]		
	operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
	print("solution : ", solution(operations))

main()
