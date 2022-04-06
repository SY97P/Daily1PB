def solution(arrows) : 
	answer = 0
	node2 = [0, 0]
	log = [node2]

	for comm in arrows :
		node1, node2 = getNode(comm, node2)
		if node1 != [] : 
			log.append(node1)
		log.append(node2)
	print(log)

	# 중복된 좌표 개수 // 2 - 갔다바로온 패턴 수 = 정답

	# 중복된 좌표 개수 // 2 까지 구하기.
	for l in log : 
		if log.count(l) > 1 :
			answer += 1
	print(answer)
	answer //= 4
	print(answer)

	# 갔다온 패턴 수 구하기. 
	pattern = [[0,4],[1,5],[2,6],[3,7],[4,0],[5,1],[6,2],[7,3]]
	for i in range(len(arrows)-1) : 
		if [arrows[i], arrows[i+1]] in pattern : 
			answer -= 1
			print([arrows[i], arrows[i+1]])
			for j in range(1,i) :
				if [arrows[i-j], arrows[i+j+1]] in pattern : 
					answer -= 1
					print([arrows[i-j], arrows[i+j+1]])
				else : 
					break

	return answer

# 모래시계 모양 때문에 대각선은 두 칸 씩 해줘야 함. 
def getNode1(comm, node) : 
	x, y = node
	if comm == 0 : 
		return [],[x, y+2]
	elif comm == 1: 
		return [x+1, y+1],[x+2, y+2]
	elif comm == 2 : 
		return [], [x+2, y]
	elif comm == 3: 
		return [x+1, y-1],[x+2, y-2]
	elif comm == 4: 
		return [], [x, y-2]
	elif comm == 5: 
		return [x-1, y-1],[x-2, y-2]
	elif comm == 6 : 
		return [],[x-2, y]
	else :
		return [x-1, y+1],[x-2, y+2]

def getNode(comm, node) : 
	x, y = node
	if comm == 0 : 
		return [x, y+1],[x, y+2]
	elif comm == 1: 
		return [x+1, y+1],[x+2, y+2]
	elif comm == 2 : 
		return [x+1, y], [x+2, y]
	elif comm == 3: 
		return [x+1, y-1],[x+2, y-2]
	elif comm == 4: 
		return [x, y-1], [x, y-2]
	elif comm == 5: 
		return [x-1, y-1],[x-2, y-2]
	elif comm == 6 : 
		return [x-1, y],[x-2, y]
	else :
		return [x-1, y+1],[x-2, y+2]
		
def main() : 
	arrows = [6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]	#3
	#arrows = [7,6,5,4,3,2,1,0,4,5,6,7,0,1,2,3]
	print("solution : ", solution(arrows))

main()