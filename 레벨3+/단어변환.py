def solution(begin, target, words) :
	if target not in words : 
		return 0
	return dfs(begin, target, words)

def dfs(begin, target, words) : 
	# print(begin, target)
	if begin == target : 
		return 1
	candi = getCandi(begin, words)
	# print(candi)

	for c in candi : 
		if target in candi : 
			return 1
		words.remove(c)
		return dfs(c, target, words) + 1
		words.append(c)


def getCandi(begin, words) : 
	result = []
	for word in words : 
		count = 0
		for i in range(len(begin)) : 
			if begin[i] != word[i] : 
				count += 1
		if count == 1 : 
			result.append(word)
	return result

def main() : 
	begin, target, words = "hit","cog",["hot", "dot", "dog", "lot", "log", "cog"] # 4
	#begin, target, words = "hit","cog",["hot", "dot", "dog", "lot", "log"]	# 0
	print("solution : ", solution(begin, target, words))

main()
