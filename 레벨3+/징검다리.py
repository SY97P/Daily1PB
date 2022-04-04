def solution(distance, rocks, n) : 
	answer = 0
	rocks.sort()
	rocks = rocks + [distance]
	# print(rocks)

	left, right = 1, distance

	while left <= right : 
		mid = (left + right) // 2
		# print("mid : ", mid)
		
		min_dist = distance
		# 해당 최소추정치보다 사이거리가 짧은 애들을 제거
		count, curr = 0, 0
		for r in rocks : 
			d = r - curr
			if d < mid : 
				count += 1
			else :
				curr = r
				min_dist = min(d, min_dist)
			# print(min_dist)

		if count <= n : 
			answer = min_dist
			left = mid + 1
		else : 
			right = mid - 1

	return answer

	
		

def main() : 
	distance, rocks, n = 25,[2, 14, 11, 21, 17],2	# 4
	#distance, rocks, n = 11,[2,8], 1				# 3
	print("solution : ", solution(distance, rocks, n))

main()
