def solution(routes) : 
	answer = 1
	routes.sort()
	start, end = -30000, 30000

	for route in routes : 
		# print("before : ", start, end)
		print(route)
		if start < route[0]  : 
			start = route[0]
		if end > route[1] : 
			end = route[1]

		# print("after : ", start, end)

		if start > end : 
			answer += 1
			start, end = route

	return answer

def main() : 
	routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]	# 2
	routes = [[3,5],[13,18],[5, 14],[15,20]]			# 2
	routes = [[-10,10], [-5, 15], [-15, -5]]			# 1
	routes = [[-100,-99],[-90,-50],[10, 10000],[-100, -99]] # 3
	print("solution : ", solution(routes))

main()
