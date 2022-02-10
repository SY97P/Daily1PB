# 해시 말고 다른 풀이
def solution(phone_book) : 
	temp = zip(phone_book, phone_book[1:])
	for t1, t2 in temp : 
		if t1.find(t2) : 
			return False
	return True

def main() : 
	phoneBook = ["119", "97674223", "1195524421"]	#false
	#phoneBook = ["123","456","789"]	#true
	#phoneBook = ["12","123","1235","567","88"]	#false
	print("solution : ", solution(phoneBook))

main()