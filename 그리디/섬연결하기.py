def solution(n, costs) :
	answer = 0
	# 비용 오름차순 정렬
	costs.sort(key = lambda x : x[2])
	# 섬 중복을 배제하기 위해서 set으로 선언
	route = set([costs[0][0]])
	while len(route) < n :
		for i, cost in enumerate(costs) :
			# print(i, cost)
			if cost[0] in route and cost[1] in route : 
				continue
			if cost[0] in route or cost[1] in route : 
				answer += cost[2] 
				route.update([cost[0], cost[1]])
				costs[i] = [-1, -1, -1]
				break
	return answer

def main() :
	n, costs = 4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
	print("solution : ", solution(n, costs))

main()