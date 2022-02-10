# from collections import defaultdict
# def solution(genres, plays) :
# 	answer = []
# 	hash_map = defaultdict(list)

# 	idx = 0
# 	for g, p in zip(genres, plays) : 
# 		hash_map[g].append([idx, p])
# 		idx += 1
# 	# print(hash_map)

# 	genre_count = []
# 	for key in hash_map.keys() : 
# 		count = 0
# 		for v in hash_map[key] :
# 			count += v[1]
# 		genre_count.append([key, count])
# 	# print(genre_count)

# 	genre_count.sort(key = lambda x : x[1], reverse = True)
# 	# print(genre_count)

# 	temp = []
# 	for genreInfo in genre_count : 
# 		genre = genreInfo[0]
# 		playInfo = hash_map[genre]
# 		playInfo.sort(key = lambda x : x[1], reverse = True)
# 		# print(playInfo)
# 		temp.append(playInfo[:2])
# 	for t in temp : 
# 		# print(t)
# 		for q in t :
# 			# print(q)
# 			answer.append(q[0])
# 	# print(answer)
# 	return answer

def solution(genres, plays) : 
	answer = []
	d = {e:[] for e in set(genres)}
	print(d)
	for e in zip(genres, plays, range(len(plays))):
		print(e)
		d[e[0]].append([e[1], e[2]])
	print(d)
	genreSort = sorted(list(d.keys()), key = lambda x : sum(map(lambda y : y[0], d[x])), reverse= True)
	print(genreSort)
	for g in genreSort : 
		temp = [e[1] for e in sorted(d[g], key = lamb)]
	


def main() : 
	genres, plays = ["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]	
	#[4, 1, 3, 0]
	print("solution : ", solution(genres, plays))

main()