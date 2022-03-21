def solution(genres, plays) : 
	answer,priority = [],[]
	heap, genres_pri = {}, {}

	for i in range(len(plays)) : 
		heap[i] = [genres[i], plays[i]]
	for h in heap.values() : 
		g, p = h
		if g not in genres_pri.keys() : 
			genres_pri[g] = 0
		genres_pri[g] += p

	for item in genres_pri.items() : 
	    priority.append(list(item))
	priority.sort(reverse = True, key = lambda x : x[1])
# 	print(priority)
	
	for g in priority : 
	    genre = g[0]
	    temp = []
	    for h in heap.items() : 
	        if h[1][0] == genre  :
	            temp.append(h)
	    if len(temp) <= 1: 
	        answer.append(temp[0][0])
	    else : 
	        temp.sort(key = lambda x : x[1][1], reverse = True)
	        for t in temp[:2] :
	            answer.append(t[0])
	return answer
		

def main() : 
	genres, plays = ["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]	
	# [4, 1, 3, 0]
	genres, plays = ["classic", "pop", "classic", "classic", "pop"],[200,600,200,200,2500]
	# [4, 1, 0, 2]
	genres, plays = ["classic"], [200]
	print("solution : ", solution(genres, plays)) 

main()