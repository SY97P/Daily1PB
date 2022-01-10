def solution(n, lost, reserve) :
	#print(n, lost, reserve)
	answer = 0
	for i in range(1, n+1) :
		if i not in reserve and i not in lost :
			answer += 1
			#print(i, " has just one")
		elif i in reserve :
			if i in lost :
				answer += 1
				reserve.remove(i)
				lost.remove(i)
			#	print(i, " bring another, but lost it")
			elif (i-1) in lost :
				answer += 2
				reserve.remove(i)
				lost.remove(i-1)
				#print(i, " lent his to former")
			elif (i+1) in lost :
				answer += 1
				reserve.remove(i)
				lost.remove(i+1)
				#print(i, " lent his descenter")
			else :
				answer += 1
				reserve.remove(i)
				#print(i , " cannot lent his, but he use it")
	return answer

def main() :
	tc1 = [5, [2,4], [1,3,5]]
	tc2 = [5, [2,4], [3]]
	tc3 = [3, [3], [1]]
	print("solution : ", solution(tc1[0], tc1[1], tc1[2]))

main()