N,B = input().split()
number = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

N = N[::-1]

answer = 0

for i in range(len(N)):
    answer += (int(B)**i) * number.index(N[i]) 
    
print(answer)