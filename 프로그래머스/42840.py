def solution(answers):
    result = []
    list1 = []
    list2 = []
    list3 = []   
    #답안 작성
    for i in range(len(answers)): #1번 수포자 1 2 3 4 5반복 삽입
        if i >= 5:
            i = i%5
        list1.append(i+1)
        i += 1

    list2num = [1,3,4,5] #2번 수포자 답 리스트
    k=0
    for i in range(len(answers)): 
        if (i+1) % 2 == 1: # 인덱스가 홀수면 2 삽입
            list2.append(2)
        else: #짝수번째면 list2num 돌면서 삽입
            if k >= 4:
                k = k%4
            list2.append(list2num[k]) 
            k += 1
    
    list3num = [3,3,1,1,2,2,4,4,5,5]  #3번 수포자 답 list
    k=0
    for i in range(len(answers)):
        if k >= 10:
            k = k%10
        list3.append(list3num[k])
        k += 1
        
   #1 2 3번 답안 작성 완.   
    # 답안 체크
    count1 = 0
    count2 = 0
    count3 = 0
    for i in range(len(answers)):
        if list1[i] == answers[i]:
            count1 += 1
        if list2[i] == answers[i]:
            count2 += 1
        if list3[i] == answers[i]:
            count3 += 1
    
    point = [count1, count2, count3]
    max_score = max(point)
    
    if count1 == max_score:
        result.append(1)
    if count2 == max_score:
        result.append(2)        
    if count3 == max_score:
        result.append(3)
    return result