n = int(input())
arr = list(map(int, input().split()))
V = [0] * (n + 1)


for i in range(n-1, -1, -1):
    V[i] = min(arr[i], V[i + 1] + 1)


print(sum(V))