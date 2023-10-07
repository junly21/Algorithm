n = int(input())
arr = list(map(int,input().split()))
V = [n-i for i in range(n)]

for i in range(n-1,-1,-1):
    if(arr[i] < V[i]):
        V[i] = arr[i]

        for j in range(i,0,-1):
            V[j-1] = V[j]+1

print(sum(V))