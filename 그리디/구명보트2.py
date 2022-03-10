def solution(people, limit) : 
	answer = 0
	i, j = 0, len(people)-1
	people = sorted(people)

	while i < j :
		small, big = people[i], people[j]
		# print(i, small, j, big)
		if small + big <= limit : 
			answer += 1
			i += 1
			j -= 1
		else : 
			answer += 1
			j -= 1

	if i == j :
		answer += 1
	return answer

def main() : 
	people, limit = [70, 50, 80, 50],100	# 3
	#people, limit = [70, 80, 50],100		# 3
	print("solution : ", solution(people, limit))

main()