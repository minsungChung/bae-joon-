def solution(phone_book):
    answer = True
    
    # phone_book 정렬
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        pre = phone_book[i]
        
        # 앞 번호가 뒷번호의 앞과 같다면
        if phone_book[i+1][:len(pre)] == pre:
            answer = False
            break
    
    return answer