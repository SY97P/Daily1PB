# 조합으로 풀면 시간초과가 나버림. 이분탐색으로 푸는 게 맞나봄. 
# import itertools
# def solution(distance, rocks, n) : 
# 	answer = 0
# 	rocks.sort()
# 	combi = list(map(list,itertools.combinations(rocks, len(rocks) - n)))
# 	min_diff = []
# 	for c in (combi) : 
# 		curr_rocks = [0] + c + [distance]
# 		# print(curr_rocks)
# 		diff = []
# 		for i in range(1, len(curr_rocks)) : 
# 			diff.append(curr_rocks[i] - curr_rocks[i-1])
# 		# print(diff, "\t", min(diff))
# 		min_diff.append(min(diff))
# 	# print(min_diff)
# 	return max(min_diff)

def solution(distance, rocks, n) : 
	answer = 0
	shortest, longest = 1, distance
	rocks.sort()
	rocks = [0] + rocks + [distance]

	while shortest <= longest : 
		mid = (shortest + longest) // 2
		# print("mid : ", mid)

		count = 0
		for i in range(1, len(rocks)) : 
			# print(rocks[i] - rocks[i-1])
			if rocks[i] - rocks[i-1] < mid : 
				count += 1
		# print("count : ", count)
		if count < n : 
			shortest = mid + 1
		else :
			answer = mid
			longest = mid - 1

	# print(answer)
	return answer
	

def main() : 
	distance, rocks, n = 25,[2, 14, 11, 21, 17],2	# 4
	print("solution : ", solution(distance, rocks, n))

main()
