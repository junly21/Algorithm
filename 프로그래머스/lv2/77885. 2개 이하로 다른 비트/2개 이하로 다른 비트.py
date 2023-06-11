def solution(numbers):
    answer = []    
    for number in numbers:
        blist = []
        flag = 0
                
        #짝수면 무조건 +1 하면 됨.
        if (number%2==0):
            answer.append(number +1)
            
        #홀수면 
        else:   
            bnum = (bin(number)[2:])
            count = 0 
            
            #다만 모두 1인경우는 앞에 0을 붙여줘야함
            for bit in bnum:    
                if bit == '1':
                    count += 1 
                if count == len(bnum):
                     bnum = '0'+bnum
                        
            #기본개념: 거꾸로 가면서 첫 01set을 10으로(역순에선 @@10@@을 @@01@@으로) 바꿔준다. 
            for bit in reversed(bnum):
                if bit == '1': 
                    blist.append(bit)
                else: #비트 0  
                    if blist[-1] == '1':
                        if flag == 0:
                            blist [-1] = '0'
                            blist.append('1')
                            flag = 1
                        else:
                            blist.append(bit)
                    else:
                        blist.append(bit)
                        
                #이러면 blist에 역순으로 되어있음.
            blist.reverse()
            
            result = "0b"+"".join(val for val in blist)
            answer.append(int(result,2))
    return answer