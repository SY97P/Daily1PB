import heapq
def solution(operations) :
	answer = []
	heap = []
	heapq.heapify(heap) 

	for o in operations :
		operation = o.split(" ")
		command, digit = operation
		print(command, digit)
		if command == 'I' : 
			heapq.heappush(heap, int(digit))
			print(heap)
		else : 
			if heap : 
				if digit == -1 : 
					heapq.heappop(heap)
				else : 
					heapq.heap
				print(heap)

	if not heap : 
		answer = [0, 0]
	else : 
		answer = [max(heap), min(heap)]
	return answer

def main() : 
	operations = ["I 16","D 1"]	# [0,0]
	operations = ["I 7","I 5","I -5","D -1"]	# [7,5]
	print("solution : ", solution(operations))

main()