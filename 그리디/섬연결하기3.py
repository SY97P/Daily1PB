def solution(n, costs) : 
	answer = 0
	visited = set()

	curr = 0
	while n >= len(visited) : 
		print("curr : ",curr)
		print("visited : ", visited)
		candi = []
		visited.add(curr)
		for c in costs : 
			if curr in (c[0], c[1]) : 
				candi.append(c)
		print("candi : ", candi)
		if not candi : 
			curr += 1
			continue
		next_info = min(candi, key = lambda x : x[2])
		costs.remove(next_info)
		answer += next_info[2]
		if next_info[0] != curr : 
			curr = next_info[0]
		else : 
			curr = next_info[1]

	return answer
			

def main() : 
	n, costs = 4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]	# 4
	print("solution : ", solution(n, costs))

main()
