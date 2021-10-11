
def solution(phone_book):
    answer = True

    phone_book = sorted(phone_book)
    
    for p1, p2 in zip(phone_book , phone_book[1:]) :
        if p2.find(p1)==0 :
            answer = False
    
    return answer


def main() :
    phone_book = ["119", "97674223", "1195524421"]

    answer = solution(phone_book)

    print(answer)
    

main()
