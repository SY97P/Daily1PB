import itertools
import math

def solution(numbers) :
	case = makeCase(numbers)
	answer = countupPrime(list(case))
	return answer

def makeCase(numbers) : 
	s = set()
	for i in range(1,len(numbers)+1) : 
		tuple_list = list(itertools.permutations(numbers, i))
		for t in tuple_list : 
			case = int(''.join(t))
			# print(case)
			if case not in (0, 1) :
				s.add(case)
	# print(s)
	return s
			

def countupPrime(case) :
	count = 0 
	for c in case : 
		if c == 2 or c == 3 : 
			count += 1
			continue
		upper_dev = int(math.sqrt(c))
		# print(upper_dev)
		isPrime = True
		for i in range(2, upper_dev+1) :
			if c % i == 0 :
				isPrime = False
				break
		if isPrime :
			count += 1
	# print(count)
	return count
			

def main() :
    numbers = "011"
    print("solution : ", solution(numbers))

main()