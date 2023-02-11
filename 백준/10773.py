N = int(input())
List = []

    
for i in range(N):
    val = int(input())
    if val ==0 :
        List.pop()
    else:
        List.append(val)

print(sum(List))



