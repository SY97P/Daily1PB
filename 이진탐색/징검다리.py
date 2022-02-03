# 징검다리 사이 거리를 기준으로 이분 탐색
# 현재 징검다리 사이 최소추정값을 기준으로 이 값보다 작은 사이 거리의 바위를 제거
# 제거된 다리 개수와 주어진 제거 개수를 비교하여 mid 수정
def solution(distance, rocks, n) :
	answer = 0 
	rocks.sort()
	rocks.append(distance)
	
	left = 1
	right = distance

	while left < right :
		mid = (left + right) // 2
		count = 0
		min_distance = distance

		curr = 0 
		for rock in rocks :
			d = rock - curr
			# print(d)
			# 최소추정값보다 징검다리 사이 길이가 적은 경우엔 해당 다리 제거 
			if d < mid :
				count += 1
			# 최소추정값보다 징검다리 사이 길이가 긴 경우에는 냅두고 이동
			else :
				curr = rock
				min_distance = min(d, min_distance)
		
		# 제거한 바위가 부족하면 더 많이 제거할 수 있도록 mid를 늘림.
		# 제거한 바위가 딱 맞으면 현재 mid값이 answer
		if count <= n : 
			answer = min_distance
			left = mid + 1

		# 제거한 바위가 더 많으면 적게 제거할 수 있도록 mid를 줄임.
		else : 
			right = mid - 1
	return answer
			

def main() :
	distance, rocks, n = 25, [2, 14, 11, 21, 17], 2	#	4
	distance, rocks, n = 25, [1, 11], 1	# 11
	print("solution : ", solution(distance, rocks, n))

main()