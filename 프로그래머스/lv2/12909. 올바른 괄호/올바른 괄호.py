def solution(s):
    answer = True
    b_list = []
    b_count = 0 
    
    #마지막이 열거나 처음이 닫으면 바로 False리턴
    # if s[-1] == '(':
    #     return False
    # elif  s[0] == ')':
    #     return False
    
    for i in s:
        if i == '(':
            b_list.append(i)
        else:
            if b_list == []:
                return False
            else: b_list.pop()
            
            
    if b_list == []:
        return True
    else:
        return False
    
    
