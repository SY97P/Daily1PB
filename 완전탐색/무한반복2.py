# 기존에 패턴을 담은 리스트의 길이를 직접 제어했다면
# 이번 풀이는 itertools 라이브러리 cycle 생성자를 이용해서 풀이
# itertools.cycle(lst)
# cycle에 사용된 인자는 순환구조 큐처럼 활용할 수 있음을 확인함.

import itertools
import heapq
def solution(answers) : 
	answer = []
	heapq.heapify(answer)
	scores = [0] * 3
	patterns = [
		itertools.cycle([i for i in range(1, 6)]),
		itertools.cycle([2,1,2,3,2,4,2,5]),
		itertools.cycle([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])
	]
	# for p in patterns : 
	# 	for i in range(10) : 
	# 		print(next(p), end = " ")
	# 	print()

	# for p in patterns : 
	# 	for i in range(10) : 
	# 		print(next(p), end = " ")
	# 	print()
	
	for a in answers : 
		for i, p in enumerate(patterns) :
			if a == next(p) : 
				scores[i] += 1

	maxScore = max(scores)
	for i, s in enumerate(scores) : 
		if s == maxScore : 
			heapq.heappush(answer, i+1)

	return answer
				
def main() : 
	wers = [1,2,3,4,5]	# [1]
	answers = [1,3,2,4,2]	# [1,2,3]
	print("solution : ", solution(answers))

main()