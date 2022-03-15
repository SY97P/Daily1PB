def solution(n, times) : 
	if len(times) == 1 :
		return n * times[0]
	answer = 0
	shortest, longest = 1, max(times) * n
	sorted(times)
	print(shortest, longest)

	while shortest <= longest : 
		mid = (shortest + longest) // 2
		print(mid)	# mid : 현재 추정하는 최소시간
		# people : 현재 추정하는 시간 동안에 처리 가능한 사람의 수
		people = 0
		for t in times : 
			people += mid // t
			if people >= n : 
				break
		if people < n : 
			answer = mid
			shortest = mid + 1
		else : 
			longest = mid - 1

	return answer + 1

def main() : 
	n, times = 6,[7, 10]	# 28
	n, times = 6,[7,10,20] 	# 21
	print("solution : ", solution(n, times))

main()
