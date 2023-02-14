N = int(input())

count_5 = 0
count_3 = 0



while(N>0):
    if N%5 == 0:
        count_5 += 1
        N = N-5
    else:
        N = N-3
        count_3 +=1

if (N >=0) :
    print(count_5+count_3)
else:
    print(-1)