# man 한테 진 애들(i_am_loser)은 man 한테 이긴 애들(i_am_winner)한테도 짐(i_am_loser.foreach.append(winner))
# man 한테 이긴 애들(winner)은 man 한테 진 애들(i_am_loser)한테 이김. (i_am_winner.foreach.append(loser))
def solution(n, results) : 
	answer = 0
	i_am_loser = [set() for i in range(n+1)]
	i_am_winner = [set() for i in range(n+1)]

	if n == 1: 
		return 1

	for r in results : 
		man1, man2 = r
		# man1 한테 진 애들 집합
		i_am_loser[man1].add(man2)
		# man2 한테 이긴 애들 집합
		i_am_winner[man2].add(man1)
		# man1 한테 진 애들(i_am_loser[man1])은 
		# man1 한테 이긴 애들(i_am_winner[man1])한테도 짐.

	# print(i_am_loser)
	# print(i_am_winner)

	for i in range(1, n+1) :
		for winner in i_am_winner[i] : 
			# print(winner, i_am_loser[winner])
			i_am_loser[winner].update(i_am_loser[i])
		for loser in i_am_loser[i] : 
			i_am_winner[loser].update(i_am_winner[i])

	# print(i_am_loser)
	# print(i_am_winner)

	for i in range(1, len(i_am_loser)) : 
		if len(i_am_loser[i]) + len(i_am_winner[i]) >= n - 1 : 
			answer += 1
	return answer

def main() :
	n, results = 5	,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]	# 2
	n, results = 3	,[[3, 2], [2, 1]]							# 3
	n, results = 1 	,[]											# 1
	n, results = 2	,[[1,2]]									# 2
	n, results = 5	,[[2,3],[1,3],[3,4],[5,4]]					# 1
	print("solution : ", solution(n, results))

main()