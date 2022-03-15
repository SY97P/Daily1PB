# 각 심사자들이 현재 주어진 시간 동안 심사할 수 있는 최대 인원을 기준으로 이분탐색하면 된다. 
def solution(n, times) :
	answer = 0
	left = 1
	right = max(times) * n

	while left < right :
		mid = (left + right) // 2
		people = 0

		for time in times : 
			people += mid // time
		
		# 현 시간 대 최대 처리 인원이 주어진 값보다 작으면 (시간이 부족한 것)
		# 현 시간 후보 최소값을 키워줘야 한다. 
		if people >= n :
			right = mid
		# 현 시간 대 최대 처리 인원이 주어진 값보다 크면 (시간이 더 많은 것)
		# 현 시간 후보 최대값을 줄어줘야 한다. 
		else :
			left = mid + 1
	answer = right
	return answer



def main() :
	n, times = 6, [7, 10]	#	28
	print("solution : ", solution(n, times))

main()