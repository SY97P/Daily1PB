# 이렇게 해도 되는데 시간초과 남. 다른 방식으로 풀어야 함. 
# import itertools
# def solution(number, k) : 
# 	candi = map(''.join, itertools.combinations(number, len(number)-k))
# 	return str(max(candi))

# 접근 자체를 다르게 해야할 것 같음
# O(n^4)가 되어서 그런 것 같음 -> O(n^2)으로 변경해야 함. 
# import itertools
# def solution(number, k) :
# 	return ''.join(max(itertools.combinations(number, len(number)-k)))

# 아예 조합함수를 사용하지 않고 큐(여기선 스택)를 이용함.
def solution(number, k) : 
	queue = []
	count = 0
	for num in number : 
		if not queue :
			queue.append(num)
			continue
		while queue :
			if queue[len(queue)-1] < num : 
				queue.pop()
				count += 1
				if not queue : 
					queue.append(num)
					break
				if count >= k : 
					break 
			else : 
				if len(queue) < len(number) - k : 
					queue.append(num)
				break
		print(num, queue)
	return ''.join(queue) if len(queue) >= len(number) - k else ''.join(queue)
				
	
def main() : 
	number, k = "1924"	,2		# "94"
	#number, k = "1231234",	3	# "3234"
	#number, k = "4177252841",4	# "775841"
	number, k = "54321", 1		# "5432"
	number, k = "54312", 1		# "5432"
	#number, k = "543112", 1     # "54312"
	#number, k = "54221123", 5	# "543"
	print("solution : ", solution(number, k))

main()