def solution(people, limit) :
	answer = 0
	people.sort()
	print(people)
	i, j = 0, len(people)-1
	while i <= j :
		answer += 1
		if people[i] + people[j] <= limit :
			i += 1
		j -= 1
	return answer
	

def main() :
	people, limit = [70, 50, 80, 50], 100	# 3
	#people, limit = [70, 50, 80], 100		# 3
	print("solution : ", solution(people, limit))

main()