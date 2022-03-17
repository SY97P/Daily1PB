def solution(distance, rocks, n) : 
	answer = 0
	shortest, longest = 1, distance
	rocks.sort()
	rocks = [0] + rocks + [distance]

	while shortest <= longest : 
		mid = (shortest + longest) // 2
		print(mid)

		# 현재 거리 최소 추정치 mid 보다 작은 것을 없앤다
		# 없앤 숫자를 없앨 숫자와 비교해서 범위를 수정한다. 
		count = 0
		for i in range(1, len(rocks))  :
			if rocks[i] - rocks[i-1] < mid : 
				count += 1

		# 없앤 애가 없앨 애보다 적으면 더 없애야 함. -> mid를 크게 -> shortest를 크게
		if count < n : 
			shortest = mid + 1
		else : 
			answer = mid
			longest = mid - 1

	return answer

def main() : 
	distance, rocks, n = 25,[2, 14, 11, 21, 17],2	# 4
	print("solution : ", solution(distance, rocks, n))

main()
