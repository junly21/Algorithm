from itertools import permutations

def check_prime(n):
    if n < 2: #1은 소수가 아니다.
        return False
    for i in range(2,int(n**0.5)+1): #루트+1
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    num = []
    converted_num = []
    for i in range(len(numbers)):
        num.append(set(permutations(numbers,i+1)))
    
    print(num)
    for n in num:
        print(n)
        for x in n:
            print(x)
            converted_num.append(int(''.join(x)))
                        
    converted_num = set(converted_num)
    print(converted_num)
    
    for i in converted_num:
        if check_prime(i):
            answer += 1
        
    
    
    return answer
    