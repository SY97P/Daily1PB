def solution(tickets) :
	answer = 0 
	tickets.sort()
	return getRoute('ICN', tickets)

def getRoute(begin, tickets) :
	# print(begin, tickets)
	if len(tickets) == 1 :
		return [tickets[0][0], tickets[0][1]]
	startlist = []
	for t in tickets : 
		startlist.append(t[0])
	for t in tickets : 
		if t[0] == begin and t[1] in startlist :
			target = t[1]
			tickets.remove(t)
			return [begin] + getRoute(target, tickets)

def main() :
	tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]	
	# ["ICN", "JFK", "HND", "IAD"]
	tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]	
	# ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
	tickets = [["ICN", "AAA"],["ICN", "BBB"],["BBB", "ICN"]]
	tickets =  [["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]
	# ["ICN", "BOO", "DOO", "BOO", "ICN", "COO", "DOO", "COO", "BOO"]
	print("solution : ", solution(tickets))

main()