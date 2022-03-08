def solution(n, lost, reserve) :
	#print(n, lost, reserve)
	lost = sorted(lost)
	reserve = sorted(reserve)
	upperEnd = max(n , max(lost), max(reserve))
	lowerEnd = upperEnd - n + 1
	#print(lowerEnd)
	#print(upperEnd)
	answer = 0
	for i in range(lowerEnd, upperEnd+1) :
		if i not in reserve and i not in lost :
			answer += 1
			#print(i, " has just one")
		elif i in reserve :
			if i in lost :
				answer += 1
				reserve.remove(i)
				lost.remove(i)
				#print(i, " bring another, but lost it")
			elif (i-1) in lost :
				if (i-1) in reserve :
					answer += 1
					reserve.remove(i)
				else :
					answer += 2
					reserve.remove(i)
					lost.remove(i-1)
					#print(i, " lent his to former")
			elif (i+1) in lost :
				if (i+1) in reserve :
					answer += 1
					reserve.remove(i)
				else :
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
	#tc1 = [5, [2,4], [1,3,5]]
	tc1 = [4, [4, 2], [3,5]]
	tc2 = [5, [2,3,4] ,[1,2,3]]
	tc3 = [7, [1,3,5], [3,4,7]]
	print("solution : ", solution(tc2[0], tc2[1], tc2[2]))

main()