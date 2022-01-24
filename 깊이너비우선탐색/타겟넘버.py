def solution(number, target) :
	# print(number, target)
	if len(number) == 1 :
		last = number.pop()
		if last == target or last == -target :
			return 1
		return 0
	return solution(number[1:], target+number[0]) + solution(number[1:], target-number[0])


def main() :
	number, target = [1, 1, 1, 1, 1], 3	# 5
	print("solution : ", solution(number, target))

main()