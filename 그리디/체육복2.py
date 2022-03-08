import copy
def solution(n, lost, reserve) : 
	answer = 0
	
	lost_temp = lost.copy()
	reserve_temp = reserve.copy()

	# 가져왔는데 도난당함
	for r in reserve_temp : 
		if r in lost_temp : 
			reserve.remove(r)
			lost.remove(r)

	# 이제 나머지 상황
	for i in range(1, n+1) : 
		# 하나만 가져옴 (가져왔는데 도난당함)
		if i not in lost and i not in reserve : 
			answer += 1
		elif i in lost : 
			# 잃어버린 애가 +1 한테 빌림
			if (i-1) in reserve :
				lost.remove(i)
				reserve.remove(i-1)
				answer += 1
			# 잃어버린 애가 -1 한테 빌림
			elif (i+1) in reserve : 
				lost.remove(i)
				reserve.remove(i+1)
				answer += 1
		# 아무도 빌려주지 않고 혼자 두 개
		elif i in reserve and i not in lost :
			answer += 1
	return answer

def main() : 
	n, lost, reserve = 5	,[2, 4]	,[1, 3, 5]	# 5
	#n, lost, reserve = 5	,[2, 4]	,[3]		# 4
	#n, lost, reserve = 3	,[3]	,[1]		# 2
	#n, lost, reserve = 2	,[1]	,[1]		# 2
	#n, lost, reserve = 2	,[1]	,[2]		# 2
	n, lost, reserve = 5	,[1,2,3,4,5], [1,2,3,4,5] # 5
	print("solution : ", solution(n, lost, reserve))

main()
