def solution(tickets) :
	answer = []
	# print(tickets)
	tickets.sort()
	# print(tickets)
	for ticket in tickets :
		if ticket[0] == 'ICN' :
			answer = dfsRoute(ticket, tickets)
	return ['ICN'] + answer	

def dfsRoute(ticket, tickets) :
	# print(ticket)
	tickets.remove(ticket)
	startlist = []
	for t in tickets :
		startlist.append(t[0])
	if not tickets :
		return [ticket[1]]
	for t in tickets : 
		if ticket[1] == t[0] and ticket[1] in startlist :
			return [ticket[1]] + dfsRoute(t, tickets)
	

def main() :
	tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]	
	# ["ICN", "JFK", "HND", "IAD"]
	tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]	
	# ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
	print("solution : ", solution(tickets))

main()