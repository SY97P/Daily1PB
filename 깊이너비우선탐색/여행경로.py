from collections import defaultdict

def solution(tickets) :
	answer = []
	routes = defaultdict(list)
	print(routes)

	for ticket in tickets :
		routes[ticket[0]].append(ticket[1])
	print(routes)

	for key in routes.keys() :
		routes[key].sort(reverse = True)
	print(routes)

	stack = ["ICN"]
	
	while stack :
		tmp = stack[-1]
		print("tmp : ", tmp)

		if not routes[tmp] :
			answer.append(stack.pop())
			print("answer : ", answer)
		else :
			stack.append(routes[tmp].pop())
			print("stack : ", stack)
	answer.reverse()

	return answer
	

def main() :
	tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]	# ["ICN", "JFK", "HND", "IAD"]

	tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]	
	# ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]

	tickets = [["ICN", "AAA"],["ICN", "BBB"],["BBB", "ICN"]]

	tickets =  [["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]
	# ["ICN", "BOO", "DOO", "BOO", "ICN", "COO", "DOO", "COO", "BOO"]

	print("solution : ", solution(tickets))

main()