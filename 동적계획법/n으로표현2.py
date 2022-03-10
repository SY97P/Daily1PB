# 주어진 숫자를 n번 조합해서 만들 수 있는 숫자를 set으로 저장해둠. 
# n회 조합마다 만들어지는 set을 검사해서 원하는 값이 나왔으면 횟수 n을 반환함. 

# 이 해답은 1번, 8번이 안 풀림. 조짐.
# -도 해줘야 하는 거였음. 야발.
def solution(N, number) : 
	if N == number : 
		return 1
	# index 편하게 하려고 0번 쓴 set도 선언
	n_set = [set() for i in range(9)]
	for i in range(1,9) :
		n_set[i].add(int(str(N)*i))
	# print(n_set)
	for i in range(1, 9) : 
		# n_set은 (n-i)_set과 (n-(n-i)-1)_set 을 조합해서 만들 수 있음. 
		for j in range(1, i) :
			# print(n_set[j])
			# print(n_set[i-j])
			for op1 in n_set[j] : 
				for op2 in n_set[i-j] : 
					n_set[i].update(
						[op1 + op2],
						[op1 * op2],
						[op1 - op2]
					)
					if op2 != 0 :
						n_set[i].add(op1//op2)
		# print("i : ", i, "	n_set[i] : ", n_set[i])
		if number in n_set[i] :
			return i
	return -1

def main() : 
	N, number = 5, 12		# 4
	# 5
	# 10, 25, 1
	# 15, 30, 6, 50, 125, 5, 2
	N, number = 2, 11		# 3
	N, number = 5, 31168 	# -1
	N, number = 2, 13131313 # -1
	#N, number = 2, 86		# 
	#N, number = 5, 26		# 4
	#N, number = 4, 17		# 4
	N, number = 1, 111111111#-1
	#N, number = 1, 1		# 1
	print("solution : ", solution(N, number))

main()