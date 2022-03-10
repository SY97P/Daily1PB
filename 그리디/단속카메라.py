def solution(routes) : 
	answer = 1
	routes.sort(key = lambda x : x[0])
	close, far = routes[0]
	print(close, far)

	for route in routes : 
		# do up close limit 
		close = route[0] if close < route[0] else close
		far = route[1] if far > route[1] else far
		print(close, far)
		if close > far : 
			answer += 1
			close, far = route
	return answer

def main() : 
	routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]	# 2
	#routes = [[-20,-4],[-19, -5],[-34,-8],[-9,-1]]		# 1
	#routes = [[0,1],[1,2],[2,3]]						# 2
	#routes = [[0,1],[2,3],[4,5]]						# 3
	print("solution : ", solution(routes))

main()
