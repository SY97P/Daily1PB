def solution(tickets) :
	size = len(tickets)
	answer = dfs(size, tickets, "ICN")
	return answer

# 꼭 return line에 재귀를 넣어줄 필요가 없었음. **
def dfs(size, tickets, start) :
	# print("start : ", start)
	candi = []
	for t in tickets : 
		if start == t[0] : 
			candi.append(t)
	# print("candi : ", candi)
	if not candi :
		# 마지막까지 왔지만 아직 남은 tickets가 있으면 돌아가야 함. 
		if tickets : 
			return ["null"]
		return [start]
	candi.sort(key = lambda x : x[1])
	for c in candi : 
		tickets.remove(c)
		recursion = [start] + dfs(size, tickets, c[1])
		# print(recursion)
		if "null" not in recursion :
			return recursion
		tickets.append(c)
	return ["null"]


def main() :
	tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]	
	# ["ICN", "JFK", "HND", "IAD"]
	
	tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], 						["ATL","SFO"]]	
	# ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]

	tickets =  [["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], 					["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]
	# ["ICN", "BOO", "DOO", "BOO", "ICN", "COO", "DOO", "COO", "BOO"]

	tickets = [["ICN", "ICN"],["ICN", "ICN"],["ICN", "ICN"]]

	tickets = [["ICN", "AOO"], ["AOO", "BOO"], ["BOO", "COO"], ["COO", "DOO"], ["DOO", "EOO"], ["EOO", "DOO"], ["DOO", "COO"], ["COO", "BOO"], ["BOO", "AOO"]]
	#["ICN", "AOO", "BOO", "COO", "DOO", "EOO", "DOO", "COO", "BOO", "AOO"]
	# ["ICN", "AOO", "BOO", "COO", "DOO", "COO","BOO","AOO",null,null]

	print("solution : ", solution(tickets))

main()