def solution(begin, target, words) :
	if target not in words : 
		return 0
	return changeOne(begin, target, words)
	

def changeOne(begin, target, words) :
	lst = oneList(begin, words)
	# print(lst)
	if target in lst :
		# print("target founded")
		return 1
	if not lst :
		# print("not this search")
		return 0
	countList = []
	if begin in words :
		words.remove(begin)
	for word in lst :
		# print(word)
		countList.append(changeOne(word, target, words))
	# print(countList)
	return 1 + min(countList)
	
def oneList(begin, words) :
	lst = []
	for word in words :
		count = 0
		for i, char in enumerate(word) :
			# print(i, char, begin[i])
			if char != begin[i] :
				count += 1
		if count == 1 :
			lst.append(word)
	return lst

def main() :
	begin, target, words = "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]	# 4
	#begin, target, words = "hit", "cog", ["hot", "dot", "dog", "lot", "log"]	# 0
	print("solution : ", solution(begin, target, words))

main()