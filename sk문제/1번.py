def solution(money, costs) :
	answer = 0
	value = [1, 5, 10, 50, 100, 500]
	# 1원당 단가를 먼저 계산하자 ㄴㄴ
	# price = []
	# for i in range(len(value)) : 
	# 	print(costs[i]/value[i])
	# 	price.append([value[i],costs[i]/value[i]])
	# print(price)
	
	curr_money = 0 
	index = len(value)-1
	while curr_money < money : 
		curr_money, temp = add_curr(costs, value, money, curr_money, value[index])
		answer += temp
		index -= 1
	return answer

# return [현재 화폐 금액, 현재 화폐주조액]
def add_curr(costs, value, money, curr_money, coin_value) :
	todo = money - curr_money
	# print("todo, coin_value : ", todo, coin_value)

	temp = [costs[i] * int(coin_value / value[i]) for i in range(len(value))]
	index = len(temp)
	for i in range(len(temp)-1, -1, -1) : 
		if temp[i] == 0 : 
			index = i
	temp = temp[:index]
	# print(temp)
			
	min_value = min(temp)
	count = 0
	while todo >= coin_value :
		curr_money += coin_value
		todo = money - curr_money
		count += 1
		# print(min_value, curr_money, todo)
	return [curr_money, min_value * count]
		

def main() : 
	# [1, 5, 10, 50, 100, 500]
	money, costs = 4578,[1, 4, 99, 35, 50, 1000]	# 2308
	money, costs = 1999,[2, 11, 20, 100, 200, 600]	# 2798
	print("solution : ", solution(money, costs))

main()
