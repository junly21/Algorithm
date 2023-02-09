N, M = map(int, input().split())
weightList = list(map(int, input().split()))

count = 0

for i in range(len(weightList)):
  for j in range(i + 1, len(weightList)):
    if weightList[i] != weightList[j]:
      count += 1

print(count)
