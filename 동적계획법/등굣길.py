def solution(m, n, puddles) :
	answer = 0
	maplist = [[0 for i in range(m)] for j in range(n)]
	for p in puddles :
		maplist[p[1]-1][p[0]-1] = -1
	maplist[0][0] = 1
	# for i in maplist : 
	# 	print(i)
	# print()
	for i in range(n) :
		for j in range(m) :
			if maplist[i][j] > 0 :
				if j+1 == m and i+1 == n :
					answer =  maplist[i][j] % 1000000007
				elif j+1 == m and maplist[i+1][j] != -1 : # 오른쪽 끝
					maplist[i+1][j] += maplist[i][j]
				elif i+1 == n and maplist[i][j+1] != -1 : #아래쪽 끝
					maplist[i][j+1] += maplist[i][j]
				else : 
					if j+1 == m or i + 1 == n :
						continue
					# 학교, 오른쪽 끝, 아래쪽 끝이 아닌경우
					# 우측, 하단 모두 갈 수 있음
					if maplist[i+1][j] != -1 : 
						maplist[i+1][j] += maplist[i][j]
					if maplist[i][j+1] != -1 :
						maplist[i][j+1] += maplist[i][j]
	# for i in maplist : 
	# 	print(i)

	return answer



def main() :
	m, n, puddles = 4, 3, [[2, 2]] #4
	m, n, puddles = 4, 3, [[2,2], [1,2]]
	m, n, puddles = 4, 3, [[1,2], [2,1]]
	m, n, puddles = 5, 4, [[3,2],[5,2],[1,3],[4,3]]
	print("solution : ", solution(m, n, puddles))

main()