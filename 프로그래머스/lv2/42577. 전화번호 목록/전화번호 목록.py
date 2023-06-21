def solution(phone_book):
    headers = {}
    
    for phone_number in phone_book:
        headers[phone_number] = 1 #딕셔너리에 폰번호 추가
      
    
    for phone_number in phone_book: #하나의 번호에서
        header = ''
        for number in phone_number: #번호를 단위로 쪼개서
            header += number  #문자열에 추가해주면서
            if header in headers and header != phone_number: #단위로 쪼갠 번호가 딕셔너리에 있으면 return False
                return False
    return True