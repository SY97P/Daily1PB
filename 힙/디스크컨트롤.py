# SJF : Shortest Job First?
import heapq
def solution(jobs) : 
	time = 0
	heapq.heapify(jobs)
	temp = heapq.nsmallest(len(jobs), jobs, key = lambda x: x[1])
	print(temp)
	
	


def main() : 
	jobs = [[0, 3], [1, 9], [2, 6]]		# 9
	jobs = [[0,9],[1,6],[2,3]]			# 
	print("solution : ", solution(jobs))

main() 