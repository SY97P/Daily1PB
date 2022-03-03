# I : Input / D : Delete 
# -1 : min  / 1 : max
# 비어있을때 D를 해도 아무 변화 x
# 같은 값이 여럿 있어도 하나만 제거됨. 
import heapq
def solution(operations) :
	answer, heap = [], []
	heapq.heapify(heap)

	while operations : 
		oper = operations.pop(0)
		comm, key = oper.split(' ')
		# print(comm, key)
		key = int(key)
		if comm == 'I' : 
			heapq.heappush(heap, key)
		else : 
			if heap : 
				if key == -1 : 
					out = heapq.heappop(heap)
					# print(out)
				else : 
					out = max(heap)
					heap.remove(out)
					# print(out)
		# print(heap)
	if heap : 
		answer = [max(heap), min(heap)]
	else : 
		answer = [0,0]
	return answer
	
def main() : 
	operations = ["I 16","D 1"]	# [0,0]
	operations = ["I 7","I 5","I -5","D -1"]	# [7,5]
	operations = ["I 7","I 5","I -5","D 1"]	# [5,-5]
	operations = ["I 7","I 5","I -5","I 7","D 1"]	# [7,-5]
	print("solution : ", solution(operations))

main()