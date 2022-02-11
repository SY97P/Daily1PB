import math
def solution(progresses, speeds) :
	answer = []
	queue = []

	for idx, p in enumerate(progresses) : 
		neededDay = math.ceil((100 - p) / speeds[idx])
		# print(neededDay)
		if not queue : 
			queue.append(neededDay)
			continue
		if max(queue) < neededDay : 
			# print(queue, neededDay)
			answer.append(len(queue))
			queue.clear()
			queue.append(neededDay)
		else : 
			queue.append(neededDay)
	answer.append(len(queue))
	queue.clear()
	return answer



def main() : 
	progresses, speeds = [93, 30, 55], [1, 30, 5]	#[2, 1]
	progresses, speeds = [95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]	#[1, 3, 2]
	print("solution : ", solution(progresses, speeds))

main()