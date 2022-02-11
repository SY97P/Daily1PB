def solution(priorities, location) :
	answer = 0
	queue = []

	for i, p in enumerate(priorities) : 
		priorities[i] = [i, p]

	# print(priorities)
	
	while priorities : 
		task = priorities[0]
		# print(task, priorities)
		if len(priorities) == 1 :
			queue.append(task)
			break
		priorities = priorities[1:]
		# print("priorities : ", priorities)
		value_list = []
		for p in priorities : 
			value_list.append(p[1])
		if task[1] >= max(value_list) :
			queue.append(task)
		else :
			priorities.append(task)
	# 	print(queue)
	# print(queue)
	for i, q in enumerate(queue) : 
		if location == q[0] : 
			answer = i
	return answer + 1

def main() : 
	priorities, location = [2, 1, 3, 2], 2	#1
	#priorities, location = [1, 1, 9, 1, 1, 1], 0	#5
	print("solution : ", solution(priorities, location))

main()