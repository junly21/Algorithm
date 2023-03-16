answer = 0
def solution(num):
    global answer
    if answer >= 500:
        answer = -1
        return answer
    if num%2==0 :
        answer += 1
        num = num/2
        solution(num)
    else:
        if num ==1:
            return answer
        else:
            num = 3*num +1
            answer += 1
            solution(num)
    return answer