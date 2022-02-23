# SJF : Shortest Job First?
# import heapq
# def solution(jobs) : 
# 	# answer : 각 task 당 대기시간
# 	# time : 현재 진행 중인 시간
# 	for i in range(len(jobs)) : 
# 		jobs[i] = [jobs[i][1], jobs[i][0]]
# 	# print(jobs)
# 	heapq.heapify(jobs)
# 	print(jobs)
# 	time, response_time = 0, []
# 	length = len(jobs)
# 	while jobs : 
# 		work_time, start_time = heapq.heappop(jobs)
# 		print(work_time, start_time)
# 		if work_time == 0 :
# 			response_time.append(0)
# 			continue
# 		if time < start_time and len(jobs) != length :
# 			time = work_time + start_time
# 			response_time.append(work_time)
# 		# 처음 시작 혹은 현재 시간이 시작 시간보다 작으면 
# 		# 현재 시간을 (소요시간 + 시작시간) 만큼 증가
# 		# 응답시간은 소요시간이 됨. 
# 		elif time == 0 : 
# 			time = work_time + start_time
# 			response_time.append(time)
		
# 		# 해야할 작업이 이미 와 있다면
# 		# 현재 시간에 소모시간을 더함
# 		# 응답 시간은 현재까지의 시간에 소모시간을 더한 후 시작시간을 빼줌
# 		else : 
# 			response_time.append(time + work_time - start_time) 
# 			time += work_time
			
# 	print(response_time)
# 	return sum(response_time) // length

import heapq
def solution(jobs) : 
	answer, now, i = 0, 0, 0
	heap = []
	heapq.heapify(heap)
	while i < len(jobs) :
		job = jobs[i]
		print(job)
		if now >= job[0] : 
			heapq.heappush(heap, job)
		now += 1
		
	
		
def main() : 
	jobs = [[0, 3], [1, 9], [2, 6]]		# 9
	jobs = [[0,9],[1,6],[2,3]]			# 11
	# SJF : (2+3) + (5 + 6 - 1) + (11 + 9 - 0) = 5 + 10 + 20 = 35
	# FCFS : (9) + (9 + 6 - 1) + (15 + 3 - 2) = 9 + 14 + 16 = 39
	jobs = [[0, 1], [1, 1], [2,1]]		# 1
	jobs = [[10, 10]]					# 20
	jobs = [[9,0],[2,4],[5,4]]			# 3
	jobs = [[9,1],[2,4],[5,4]]			# [2,4,5] 3
	print("solution : ", solution(jobs))

main() 