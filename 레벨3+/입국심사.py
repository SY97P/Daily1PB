# 이분탐색은 어떤 항목을 기준으로 나눌 것인지에 대해서 항상 고민해야 함. 
# 이번 문제에서의 기준점은 사람을 몇명이나 할 수 있을지에 대해서 하자.
def solution(n, times) : 
	answer = 0
	shortest, longest = 1, max(times) * n
	times.sort()

	while shortest < longest : 
		mid = (shortest + longest) // 2
		people = 0
		for t in times : 
			people += mid // t

		# print(mid, people)

		if people < n :
			shortest = mid + 1
		else :
			longest = mid

	return longest
	

def main() : 
	n, times = 6,[7, 10]		# 28
	n, times = 6,[7,9,10]		# 20
	#n, times = 6,[7,100]		# 42
	print("solution : ",solution(n, times))

main()

