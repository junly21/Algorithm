def solution(brown, yellow):
    answer = []
    total = brown + yellow
    
    height=3
    width=3
    while(1):
        if total % height != 0:
            height += 1
            continue
        else:
            width = total / height
        
        if (width-2)*(height-2) != yellow:
            height += 1
        else :
            answer.append(width)
            answer.append(height)
            print(answer)
            return answer
