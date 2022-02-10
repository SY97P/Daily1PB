from collections import defaultdict
def solution(participant, completion) :
	answer = ""
	hash_map = defaultdict(int)
	for p in participant :
		hash_map[p] += 1
	# print(hash_map)
	for c in completion :
		hash_map[c] -= 1
	for key in hash_map.keys() : 
		if hash_map[key] > 0 :
			answer = key
	return answer


def main() :
	participant, completion = ["leo", "kiki", "eden"],["eden", "kiki"]	# "leo"
	participant, completion = ["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"]	# "vinko"
	#participant, completion = ["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]		#"mislav"
	print("solution : ", solution(participant, completion))

main()