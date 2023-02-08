NX = list(input().split())
N = int(NX[0])
X = int(NX[1])

List = list(map(int, input().split()))

for i in range(0, N):
  if List[i] < X:
    print(List[i], end=" ")
