
n = int(input())

arr = list(map(int,input().split()))
V = [n-i for i in range(n)]
# arr.reverse()
# V.reverse()

#arr = [23 7 1 5]
#V = [4 3 2 1]

#arr = [4 2 1 2 2 1]
#  V = [6 5 4 3 2 1]

#step1 n=6 i=3 n-i=3 V[5 4 3 2 2 1] 
#setp2 n=6 i=2 
for i in range(n-1,-1,-1):
    if(arr[i] < V[i]):
        V[i] = arr[i]
        # print(V)

        for j in range(i,0,-1):
            V[j-1] = V[j]+1
            #print(V)
#print(V)
print(sum(V))