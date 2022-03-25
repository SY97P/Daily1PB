def solution(N, number) : 

	if N == number : 
		return 1
	answer = 0
	n_time = [set() for i in range(9)]
	for i in range(1, len(n_time)) : 
		n_time[i].add(int(str(N)*i))
	# print(n_time)

	# 2 = 1 * 1
	# 3 = 1 * 2 + 2 * 1
	for i in range(2, 9) : 
		for j in range(1,i) : 
			for op1 in n_time[j] : 
				for op2 in n_time[i-j] : 
					if op2 != 0 : 
						n_time[i].add(op1//op2)
					n_time[i].update([op1+op2, op1-op2, op1*op2])
		# print(i, n_time[i])
		if number in n_time[i] : 
			return i
	return -1

def main() : 
	N, number = 5,12	# 4
	N, number = 2,11	# 3
	N, number = 2, 22222222 # 8
	N, number = 2, 222222222 # -1
	print("solution : ", solution(N, number))

main()

