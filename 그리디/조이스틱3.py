def solution(name) : 
	answer = dfs(name, 0)
	return answer

# 현재 위치 index에서 left / right 중 짧은 쪽이랑 얼마나 작은지를 넘김
# return [방향, diff]
def shortest(name, index) :
	left, right = 0, 0
	name_temp = name[index+1:] + name[:index]
	for i, n in enumerate(name_temp, start = 1) : 
		# print("right : ",i, n)
		if n != 'A' :
			right = i
			break
	for i, n in enumerate(name_temp[::-1], start = 1) :
		# print("left : ", i, n)
		if n != 'A' :
			left = i
			break
	return [0,left, 1, right] if left < right else [1,right, 0, left]
	
# A가 아닌 가장 가까운 애를 찾아야 함.
# left와 right를 구해서 둘 중 작은 쪽으로 진행해야 함. 
def dfs(name, curr_position) : 
	position = curr_position % len(name)
	updown = alphaCount(name[position])
	leftright = shortest(name, position)
	# print("position : ", position, "updown : ", updown, "leftright : ", leftright)

	# 현재 위치 글자를 A로 바꿔줌
	lst = list(name)
	lst[position] = 'A'
	name = ''.join(lst)
	# print()
	# print(name)

	# end condition 
	if leftright[1] == 0 : 
		return updown
	# go left
	if leftright[0] == 0 :
		return updown + min(dfs(name, curr_position - leftright[1]) + leftright[1], dfs(name, curr_position + leftright[3]) + leftright[3])
	else :
		return updown + min(dfs(name, curr_position + leftright[1]) + leftright[1], dfs(name, curr_position - leftright[3]) + leftright[3])

def alphaCount(c) :
	down = ord(c) - ord('A')
	up = ord('Z') - ord(c) + 1	
	# print("down : ", down, "up : ", up)
	return down if down <= up else up

def main() : 
	name = "JEROEN"	# 56
	#name = "JAN"	# 23
	name = "AAA"	# 0
	name = "A"		# 0
	name = "JAZ"	# 11
	name = "JAAAZA" # 12
	name = "ABAAAAAAAAABB" # 7
	name = "ABABAAAAAAABA" # 10
	#name = "BBBAAAAB" # 8
	print("solution : ", solution(name))

main()