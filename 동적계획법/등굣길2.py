def solution(m, n, puddles) : 
	answer = 0
	way = [[0 for i in range(m)] for j in range(n)]
	way[0][0] = 1
	for p in puddles : 
		way[p[1]-1][p[0]-1] = -1 
	# print(way)

	for i in range(n) : 
		for j in range(m) : 
			if way[i][j] == -1 : 
				continue
			right_already, down_already = True, True
			try : 
				# print("try")
				# 아래쪽 애에게 나를 증가
				if way[i+1][j] != -1 : 
					# print("아래쪽 애 증가")
					way[i+1][j] += way[i][j]
					down_already = False
				# 오른쪽 애에게 나를 증가
				if way[i][j+1] != -1 : 
					# print("오른쪽 애 증가")
					way[i][j+1] += way[i][j]
					right_already = False
			except : 
				# print("except")
				# 학교인 경우
				if i == n-1 and j == m-1 : 
					# print("학교인 경우")
					answer = way[i][j]
					break
				# 아래쪽 끝인 경우 (학교 아님)	
				elif i == n-1 and j != m-1 and right_already : 
					# print("아래쪽 끝인 경우 -> 오른쪽만 증가")
					if way[i][j+1] != -1 : 
						way[i][j+1] += way[i][j]
				# 오른쪽 끝인 경우 (학교 아님)
				elif i != n-1 and j == m-1 and down_already : 
					# print("오른쪽 끝인 경우 -> 아래쪽만 증가")
					if way[i+1][j] != -1 : 
						way[i+1][j] += way[i][j]

	# for i in range(n) : 
	# 	for j in range(m) : 
	# 		print(way[i][j],end = "\t")
	# 	print()
	return answer % 1000000007
			
				



def main() : 
	m, n, puddles = 4,3,[[2, 2]]	# 4
	m, n, puddles = 5,3,[[2,2],[3,1]] # 
	print("solution : ", solution(m, n, puddles))

	# [1, 1, 1, 1],
	# [1,-1, 1, 2],
	# [1, 1, 2, 4]

	# 1 0 0 0 0
	# 0  0 0 0 
	# 0 0 0 0 0
	#

main()
