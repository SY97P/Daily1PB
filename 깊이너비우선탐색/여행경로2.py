def solution(tickets) :
	answer = []
	route = dict()
	
	route['a'] = "a"
	route['a'].append("b")

	print(route)
			


def main() :
	tickets =  [["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]
	# ["ICN", "BOO", "DOO", "BOO", "ICN", "COO", "DOO", "COO", "BOO"]

	print("solution : ", solution(tickets))

main()