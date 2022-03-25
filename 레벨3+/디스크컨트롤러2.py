import heapq
def solution(jobs) : 
	answer = []
	jobs.sort()
	# print(jobs)
	ready = []
	heapq.heapify(ready)

	time = 0
	while True : 
		if not jobs and not ready : 
			break
		# 현재시간 기준으로 대기 중인 작업만 temp로 가져와야 함. 
		temp = jobs.copy()
		for j in jobs :
			if time >= j[0] : 
				heapq.heappush(ready, [j[1],j[0]])
				temp.remove(j)
		jobs = temp
		print("앞으로 더 해야 할 거 : ", jobs)

		if not ready : 
			time += 1
			continue
				
		print("지금 대기 중인 거 : ", ready)
		# 현재 대기 중인 작업 중에서 가장 걸리는 시간이 짧은 애(SJF)
		curr_job = heapq.heappop(ready)
		print("curr_job : ", curr_job)

		work_time, start_time = curr_job
		# 현재시간이 시작시간보다 작으면 기다렸다가 작업함.
		if time <= start_time : 
			time = start_time
		# 응답시간 = 작업이 완료된 현재시간 - 시작시간
		time += work_time
		response_time = time - start_time
		answer.append(response_time)
	return sum(answer) // len(answer)
				
		

def main() : 
	jobs = [[0, 3], [1, 9], [2, 6]]		# 9
	jobs = [[0,3], [2,1], [1, 10]]		# SJF : (3+6+15)//3=8 MIXED : (3+2+13)//3=6 
	jobs = [[10, 9]]					# 9
	print("solution : ", solution(jobs))

main()


# SJF로만 푸니까 못 풀게 되는 것.
# FCFS가 주효한 경우가 있다. 
# 실시간으로 SJF를 적용할 수 있도록 해야 함.
# import heapq
# def solution(jobs) : 
# 	answer = []
# 	temp = []
# 	heapq.heapify(temp)
# 	for j in jobs : 
# 		item = [j[1], j[0]]
# 		heapq.heappush(temp, item)
# 	# print(temp)
# 	time = 0	# 현재 시간
# 	while temp : 
# 		curr = heapq.heappop(temp)
# 		# print(curr)
# 		work_time, start_time = curr
# 		# 현재시간이 시작시간보다 작거나 같으면 시작시간만큼 기다렸다가 작업함. 
# 		if time <= start_time : 
# 			time = start_time
# 		# 중요한 건 각 작업별로 얼만큼의 시간을 기다려야 하는가
# 		# 응답시간 = 작업이 끝난 현재 시간 - 시작시간
# 		time += work_time
# 		response_time = time - start_time
# 		answer.append(response_time)
# 		#현재시간이 시작시간보다 크면 현재 작업 종료시점만큼 기다렸다가 작업함. 
# 		# print(time, response_time)
# 	return sum(answer) // len(answer)
