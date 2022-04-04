def solution(tickets) : 
	start = "ICN"
	tickets.sort()
	return dfs(start, tickets)

def dfs(start, tickets) : 
	candi = getCandi(start, tickets) 

	if not tickets : 
		return [start]

	for c in candi : 
		tickets.remove(c)
		temp = dfs(c[1], tickets)
		if temp != [] : 
			return [c[0]] + temp 
		tickets.append(c)

	return []

def getCandi(start, tickets) : 
	result = []
	for t in tickets : 
		if t[0] == start : 
			result.append(t)
	return result

def main() : 
	tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]	
	# ["ICN", "JFK", "HND", "IAD"]
	tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]	
	# ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
	tickets = [["A","B"],["B","D"],["D","C"],["C","D"],["D","B"],["B","C"]]
	print("solution : ", solution(tickets))

main()
