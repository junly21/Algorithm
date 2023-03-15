def solution(phone_number):
    num_list = list(phone_number)
    new_phone_number=""
    for i in range(len(phone_number)):
        if i <= len(phone_number)-5:
            num_list[i] = '*'
    for i in num_list:
        new_phone_number += i 
    print(new_phone_number)
    answer = new_phone_number
    return answer