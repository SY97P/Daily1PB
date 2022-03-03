# 주어진 숫자를 조합해서 만들 수 있는 가장 큰 수를 반환
def solution(numbers) : 
	answer = ""
	nums = []
	for n in numbers : 
		# 모든 숫자를 #### 포맷으로 맞춰줌
		num = str(n)
		length = len(num)
		while len(num) < 4 : 
			num = num * 2
		num = num[:4]
		nums.append([num, length])
	# print(nums)
	nums.sort(reverse = True)
	# print(nums)
	for n in nums : 
		number = n[0][:n[1]]
		answer += number
	return str(int(answer))
			

def main() : 
	numbers = [6, 10, 2]	# "6210"
	#numbers = [3, 30, 34, 5, 9]	# "9534330"
	numbers = [0, 0]		# 0
	numbers = [3, 30, 31]	# 33130
	print("solution : ", solution(numbers))

main()
