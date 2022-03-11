def solution(money) : 
	# 첫 번째 집을 무조건 터는 경우
	dp1 = [0 for i in range(len(money))]
	dp1[0] = money[0]
	dp1[1] = max(money[0], money[1])

	for i in range(2, len(money)-1) : 
		dp1[i] = max(dp1[i-1], dp1[i-2] + money[i])

	# 두 번째 집을 무조건 터는 경우
	dp2 = [0 for i in range(len(money))]
	dp2[0] = 0
	dp2[1] = money[1]

	for i in range(2, len(money)) : 
		dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])

	# print(dp1)
	# print(dp2)
	return max(max(dp1), max(dp2))

def main() : 
	money = [1, 2, 3, 1]	# 4
	print("solution : ", solution(money))

main()