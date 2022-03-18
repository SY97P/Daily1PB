def solution(arrows) : 
	answer = 0
	curr = [0,0]
	log = [curr]
	
	for code in arrows : 
		curr1, curr = getCoordination(code, curr)
		# print(curr)
		if curr1 != [] :
			log.append(curr1)
		log.append(curr)
		
	print(log)

	invalid_count = getInValidCount(arrows)
	print(invalid_count)
	
	for l in log : 
		if log.count(l) >= 2 : 
			answer += 1
	print(answer)
	return answer // 2 - (invalid_count)
	

def getInValidCount(log) : 
	invalid_pattern = {0:4,1:5,2:6,3:7,4:0,5:1,6:2,7:3}

	count = 0
	for i in range(len(log)-1) : 
		# invalid pattern이 나오면 여기부터 invalid_pattern이 아닐 때까지 count 늘림 
		if invalid_pattern[log[i]] == log[i+1] : 
			count += 1
			for j in range(1, i+1) :
				if invalid_pattern[log[i-j]] == log[i+1+j] :
					count += 1
				else : 
					break 
	return count

def getCoordination(code, curr) :
	if code == 0 : 
		return [],[curr[0], curr[1]+2]
	elif code == 1: 
		return [curr[0]+1, curr[1]+1],[curr[0]+2, curr[1]+2]
	elif code == 2: 
		return [],[curr[0]+2, curr[1]]
	elif code == 3 :
		return [curr[0]+1,curr[1]-1],[curr[0]+2, curr[1]-2]
	elif code == 4 : 
		return [],[curr[0], curr[1]-2]
	elif code == 5 : 
		return [curr[0]-1, curr[1]-1],[curr[0]-2, curr[1]-2]
	elif code == 6 :
		return [],[curr[0]-2, curr[1]]
	elif code == 7 : 
		return [curr[0]-1, curr[1]+1],[curr[0]-2, curr[1]+2]
	else : 
		return []

def main() : 
	arrows = [6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]	# 3
	#arrows = [2,3,3,4,1,5,6,7,4,2,3,1,5,4]								# 1
	arrows = [1,5]														# 0
	arrows = [1]														# 0
	arrows = [0,2,4,6]													# 1
	arrows = [0,2,4,6,5,2,2,2,0,0,0,6,6,6,4,4,4]						# 2
	arrows = [6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0, 6] # 4
	arrows = [1,2,3,4,5,6,7,5,1,2,4,3,6,2,1,4,7,5,1,2,6,3,4,2]
	arrows = [4,2,0,6,3,0,5]											# 4
	#arrows = [6, 5, 2, 7, 1, 4, 2, 4, 6]
	#arrows = [5, 2, 7, 1, 6, 3]
	#arrows = [6, 2, 4, 0, 5, 0, 6, 4, 2, 4, 2, 0]
	print("solution : ", solution(arrows))

main()