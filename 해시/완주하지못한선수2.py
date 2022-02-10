# 해시 이용하지 않는 다른 풀이
import collections
def solution(participant, completion) : 
	answer = collections.Counter(participant) - collections.Counter(completion)
	return list(answer)[0]

def main() :
	participant, completion = ["leo", "kiki", "eden"],["eden", "kiki"]	# "leo"
	participant, completion = ["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"]	# "vinko"
	#participant, completion = ["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]		#"mislav"
	print("solution : ", solution(participant, completion))

main()