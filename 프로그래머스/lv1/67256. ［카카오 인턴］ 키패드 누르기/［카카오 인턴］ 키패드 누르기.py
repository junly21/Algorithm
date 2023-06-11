

def solution(numbers, hand):
    answer = ''
    key_pattern = {'L':(1,4,7), 'R':(3,6,9)}
    left_hand = [0,3]
    right_hand = [2,3]
    location = [0,0]
    for number in numbers:
        #keypattern에 있는지 판단.
        #없으면 최근 손 불러와서 거리계산
        #가까운데 찍고 손 저장
        if number in key_pattern['L']:
            
            answer += 'L'
            #left_hand최신화
            if number == 1:
                left_hand = [0,0]
            elif number == 4:
                left_hand = [0,1]
            elif number == 7:
                left_hand = [0,2]
            else:
                print('예외발생L')
                
        elif number in key_pattern['R']:
            answer += 'R'
             #right_hand최신화
            if number == 3:
                right_hand = [2,0]
            elif number == 6:
                right_hand = [2,1]
            elif number == 9:
                right_hand = [2,2]
            else:
                print('예외발생R')
            
        else: #2 5 8 0 처리하기
            if number == 2:
                location = [1,0]
            elif number == 5:
                location = [1,1]
            elif number == 8:
                location = [1,2]
            elif number == 0:
                location = [1,3]
                
            distance_L = abs(location[0]-left_hand[0]) + abs(location[1]-left_hand[1])
            distance_R = abs(location[0]-right_hand[0]) + abs(location[1]-right_hand[1])
            
            if distance_L < distance_R:
                answer += "L"
                left_hand = location
            elif distance_L == distance_R:
                if hand =='left':
                    answer +="L"
                    left_hand = location
                else:
                    answer +="R"
                    right_hand = location
                    
            else:
                answer += "R"
                right_hand = location
    return answer