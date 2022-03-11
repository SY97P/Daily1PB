def solution(begin, target, words) :
	if target not in words : 
		return 0 
	return dfs(begin, target, words)

def dfs(begin, target, words) : 
	if begin == target : 
		return 0
	candi = oneChanged(begin, words)
	if not candi : 
		return 0
	count_list = []
	for c in candi : 
		words.remove(c)
		count_list.append(dfs(c, target, words))
	return 1 + min(count_list)

def oneChanged(begin, words) : 
	result = []
	for word in words : 
		count = 0 
		for i in range(len(word)) : 
			if begin[i] != word[i] : 
				count += 1
		if count == 1 : 
			result.append(word)
	return result
	

def main() : 
	begin, target, words = "hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]	#4
	#begin, target, words = "hit","cog",["hot", "dot", "dog", "lot", "log"]	# 0
	print("solution : ", solution(begin, target, words))

main()