def solution(name) :
	answer = 0
	# 'A' = 65 'Z' = 91
	alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	# #print(len(alphabet))
	# for idx, item in enumerate(name) : 
	# 	#print(idx, item)
	# 	if (item == 'A') :
	# 		answer += 1
	# 	else :
	# 		forward = ord(item) - 65
	# 		backward = 91 - ord(item)
	# 		#print(forward, backward)
	# 		answer += min(forward, backward) + 1

	# 		front, back = 0, 0
	# 		for i in range(1, len(name)+1) :
	# 			if (name[(idx + i) % len(name)] != 'A') :
	# 				front = i
	# 				break
	# 		for i in range(1, len(name)+1) :
	# 			if (name[(idx - i)] != 'A') :
	# 				back = i
	# 				break
	# 		#print(item, front, back)
	# 		if front < back : 
	index = 0
	count = 0
	while count < len(name) :
		if name[index] == 'A' :
			answer += 1
			count += 1
		else :
			forward = ord(name[index]) - 65
			backward = 91 - ord(name[index])
			answer += min(forward, backward) + 1
			count += 1

			front, back = 0, 0
			for i in range(1, len(name) + 1) :
				if (name[(index + i) % len(name)] != 'A') :
					front = i
					break
			for i in range(1, len(name) + 1) :
				if (name[(index - i)] != 'A') :
					back = i
					break
			if (front < back) : 
				index += front
			else :
				index -= back
			print(index, name[index])

				
			
	return answer-1


def main() :
	#name = "JAZ" # 11
	#name = "JEROEN" # 56
	#name = "JAN" # 23
	name = "JAAAAZ" # 11
	#name = "JAJAZA"
	print("solution : ", solution(name))

main()