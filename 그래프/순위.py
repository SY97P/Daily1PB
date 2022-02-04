from collections import defaultdict

def solution(n, results) :
	answer = 0
	# 패배시킨 애들은 누구를 이겼나
	losersTo = defaultdict(set)
	# 패배한 애들이 누구한테 패배했나
	winnersTo = defaultdict(set)

	for winner, loser in results : 
		# print(winner, loser)
		losersTo[winner].add(loser)
		winnersTo[loser].add(winner)
	
	# print(losersTo)
	# print(winnersTo)

	for i in range(1, n+1) :
		# i한테 진 애들은 i가 진 애들한테 다 짐.
		# i한테 진 애들은 i한테 이긴 애들이 이김. 
		for loser in losersTo[i] : 
			winnersTo[loser].update(winnersTo[i])
		# i한테 이긴 애들은 i가 진 애들한테 다 이김
		for winner in winnersTo[i] : 
			losersTo[winner].update(losersTo[i])

	# 이기고 진 애들을 모두 합한 게 총원보다 1 모자라면 순위를 아는 것.
	for i in range(1, n+1) :
		if len(losersTo[i]) + len(winnersTo[i]) == n - 1 :
			answer += 1
	return answer

def main() :
	n, results = 5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]	# 2
	print("solution : ", solution(n, results))

main()