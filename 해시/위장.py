from collections import defaultdict
def solution(clothes) :
	answer = 1
	hash_map = defaultdict(int)
	
	for c in clothes : 
		hash_map[c[1]] += 1
		
	if len(hash_map.keys()) == 1 : 
		print("key count is 1")
		return hash_map[list(hash_map.keys())[0]]
	
	# 각 value에 1을 더한걸 곱하는 게 답이 됨. (경우의 수 공식)
	for value in hash_map.values() : 
		answer *= (value + 1)
	# 아무것도 안 입는 경우는 제외해야 함. 
	return answer - 1
		
	
def main() : 
	clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]	#5
	#clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]	#3
	clothes = [["a", "top"], ["b","middle"], ["c", "bottom"]] # 7
	print("solution :  ", solution(clothes))

main()