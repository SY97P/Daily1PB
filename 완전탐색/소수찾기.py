from itertools import permutations
import math

def solution(numbers) :
    lst = list(set(makeCase(numbers)))
    #print(lst)
    answer = 0
    for item in lst :
        isPrime = True
        if (item < 2) :
            continue
        for i in range(2, int(math.sqrt(item))+1) :
            if (item % i == 0) :
                #print(item)
                isPrime = False
                break
        #print(item)
        if (isPrime) :
            answer += 1
    return answer



def makeCase(numbers) :
    case = list(numbers)
    #print(case)
    for i in range(2, len(numbers)+1) :
        per = list(permutations(list(numbers), i))
        #print(per)
        for i in per :
            case.append(''.join(i))
    #print(case)
    return list(map(int, case))

  

def main() :
    numbers = "011"
    #print("solution : ", solution(numbers))

main()