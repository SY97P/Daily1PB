def solution(phone_book) :
	answer = True
	hash_map = dict()
	for phone_number in phone_book : 
		hash_map[phone_number] = 1
	# print(hash_map)
	for phone_number in phone_book : 
		temp = ""
		for digit in phone_number : 
			temp += digit
			# print("phone_number : ", phone_number, "temp : ", temp)
			# 현재 번호로 만든 prefix가 현재 번호와 같으면 안 됨. 
			# 또한 만든 prefix가 hash_map에 존재해야 함. key, value 둘 중 하나만이라도 일치하는게 있으면 됨. 
			if temp != phone_number and temp in hash_map : 
				return False
	return True

def main() : 
	phoneBook = ["119", "97674223", "1195524421"]	#false
	#phoneBook = ["123","456","789"]	#true
	#phoneBook = ["12","123","1235","567","88"]	#false
	print("solution : ", solution(phoneBook))

main()