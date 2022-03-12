def solution(n, clockwise) : 
	answer = [[0 for i in range(n)] for i in range(n)]

	# 귀찮은 애들 먼저 처리
	if (n == 1) : 
		return [[1]]
	elif n == 2: 
		return [[1,1],[1,1]]
	elif n == 3 : 
		return [[1,2,1],[2,3,2],[1,2,1]]
	elif n == 4 : 
		return [[1,2,3,1],[3,4,4,2],[2,4,4,3],[1,3,2,1]]

	# 끄트머리 처리
	for i in range(n-1) : 
		answer[0][i], answer[i][n-1], answer[n-1][n-1-i], answer[n-1-i][0] = i+1, i+1, i+1, i+1
		print(n/2 - (i+1))
		if 2 * i <= n : 
			answer[1][1+i], answer[i+1][n-2], answer[n-2][n-2-i], answer[n-2-i][1] = n+i,n+i,n+i,n+i
	
	sub, index = 3, 2
	value = n
	while sub + 1 < n : 
		value += n - sub
		answer[index][index],answer[n-(index+1)][index],answer[index][n-(index+1)],answer[n-(index+1)][n-(index+1)] = value, value, value, value
		sub += 2
		index += 1

	# True : 시계 False : 반시계
	if clockwise : 
		answer = makeClock(n, answer)
	else : 
		answer = makeAntiClock(n)

	for a in answer : 
		print(a)
	return answer

def makeClock(n, answer) : 
				
	return answer

def makeAntiClock(n) : 
	return []

def main() : 
	n, clockwise = 5,True	
	#[[1,2,3,4,1],[4,5,6,5,2],[3,6,7,6,3],[2,5,6,5,4],[1,4,3,2,1]]

	n, clockwise = 7, True
	n, clockwise = 9, True
	# n, clockwise = 6,False	
	#[[1,5,4,3,2,1],[2,6,8,7,6,5],[3,7,9,9,8,4],[4,8,9,9,7,3],[5,6,7,8,6,2],[1,2,3,4,5,1]]
	
	# n, clockwise = 9,False	
	#[[1,8,7,6,5,4,3,2,1],[2,9,14,13,12,11,10,9,8],[3,10,15,18,17,16,15,14,7],	
	#[4,11,16,19,20,19,18,13,6],[5,12,17,20,21,20,17,12,5],[6,13,18,19,20,19,16,11,4],
	#[7,14,15,16,17,18,15,10,3],[8,9,10,11,12,13,14,9,2],[1,2,3,4,5,6,7,8,1]]
	print("solution : ", solution(n, clockwise))

main()
