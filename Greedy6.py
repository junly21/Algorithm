food_times = list(map(int,input().split()))
k = int(input())
sec = 0
answer =0
ok = False
while(1):
    i=0
    for i in range(len(food_times)):
        if food_times[i] <= 0:
            continue
        food_times[i] -= 1
        sec += 1
        if sec == k :
            if i ==len(food_times)-1:
                for j in food_times:
                    if j >=1:
                        answer=j
                        ok = True
                        break;
            else:
                for j in range(i+1,len(food_times)):
                    if j>=1:
                        answer=j+1
                        ok = True
                        break;
                    
            break;
    if ok == True:
        break;
    
print(answer)    
    