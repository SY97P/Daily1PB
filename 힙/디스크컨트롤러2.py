import heapq
def solution(jobs) : 
	answer = 0 
	temp = []
	heapq.heapify(temp)
	for j in jobs : 
		item = [j[1], j[0]]
		heapq.heappush(temp, item)
	# print(temp)
	while temp : 
		curr = heapq.heappop(temp)
		print(curr)
		time, clock = curr
		

def main() : 
	jobs = [[0, 3], [1, 9], [2, 6]]		# 9
	print("solution : ", solution(jobs))

main()