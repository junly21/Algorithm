def solution(brown, yellow):
    answer = []
    total = brown + yellow
    
    height=3
    width=3 #최소 3x3은 되어야함
    
    while(1):
        if total % height != 0: #높이랑 안나누어떨어지면 정수 될때까지 나눠
            height += 1
            continue
        else: #나누어떨어지면 width랑 height를 정해보자
            width = total / height
        
        if (width-2)*(height-2) != yellow: #넓-2 x 높-2 가 옐로면 정답인거고 아니면 높이 추가해보자
            height += 1
        else :
            answer.append(width)
            answer.append(height)
            print(answer)
            return answer

