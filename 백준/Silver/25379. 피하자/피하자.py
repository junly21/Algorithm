n = int(input())
arr = list(map(int,input().split()))
arr2 = []
for num in arr:
  arr2.append(num)

length = len(arr)
evenCnt = 0
oddCnt = 0
oddChange = 0
evenChange = 0


for i in range(0,length):
  if arr[i] % 2 != 0:
    oddCnt += 1
  if arr2[i] % 2 == 0:
     oddChange += oddCnt

for i in range(0,length):
  if arr2[i] % 2 == 0:
    evenCnt += 1
  if arr2[i] % 2 != 0:
     evenChange += evenCnt

      
print(min(oddChange, evenChange))
