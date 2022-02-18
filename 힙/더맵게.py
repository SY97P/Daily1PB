# 섞은 음식의 스코빌 지수 
#	= 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
import heapq
def solution(scoville, k) : 
	answer = 0
	heapq.heapify(scoville)
	while scoville[0] < k :
		# print(scoville)
		if len(scoville) == 1 : 
			return -1
		answer += 1
		first = heapq.heappop(scoville)
		second = heapq.heappop(scoville)
		mixed = first + second * 2
		# print(first, second, mixed)
		heapq.heappush(scoville, mixed)
	
	return answer
		

def main() : 
	scoville, k = [1, 2, 3, 9, 10, 12], 7	# 2
	scoville, k = [3, 5, 1, 2, 3, 5], 5		# 2
	print("solution : ", solution(scoville, k))

main() 