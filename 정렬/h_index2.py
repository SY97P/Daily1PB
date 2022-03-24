# 어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.
# 인용된 논문수 : h 이상. 나머지 논문 수 : n-h 이하(h이하) -> n-h <= h
def solution(citations) : 
	answer = 0
	citations.sort(reverse = True)
	h = 0
	while True : 
		print("h : ", h, " citations[h] : ", citations[h])
		# citations[h] : h번 이상 인용된 논문의 정확한 인용횟수
		if h < citations[h] :
			# if len(citations)-h <= h :
			# 	return h
			h += 1
		else : 
			if len(citations)-1-h < h :
				return h
			return h - 1 if h > 0 else 0

def main() : 
	citations = [3, 0, 6, 1, 5]		# 3
	#citations = [4,65,1,243,0]		# 3
	#citations = [0, 1, 1, 2, 2]     # 1
	citations = [1,1,1]				# 0
	citations = [0,0,0]			 # 0
	citations = [0, 1, 1]			# 1
	print("solution : ", solution(citations))

main()
