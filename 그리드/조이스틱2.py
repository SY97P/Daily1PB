# 주어진 글자를 최소 조작으로 만들 수 있는지 
# 초기에는 A로만 되어있는 글자가 주어진다.

def solution(name) :
	answer = 0
	modified = [min(ord(char)-ord('A'), ord('Z')-ord(char)+1) for char in name]
	print(modified)
	idx = 0
	while True :
		answer += modified[idx]
		modified[idx] = 0

		if sum(modified) == 0 :
			break
		
		left, right = 1, 1
		while modified[idx-left] == 0 and idx-left < len(name) :
			left += 1
		while modified[idx+right] == 0 and idx+right < len(name) :
			right += 1
		idx += -left if left < right else right
		answer += left if left < right else right
	return answer

def main() :
	name = "JAZ" # 11
	name = "JEROEN" # 56
	#name = "JAN" # 23
	#name = "JAAAAZ" # 11
	#name = "JAJAZA"
	print("solution : ", solution(name))

main()