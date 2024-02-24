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
for num in arr:
  if num % 2 == 0:
    evenCnt += 1
  else: 
    oddCnt +=1

def isOdd(arr):
  for i in range(0,oddCnt):
    if arr[i] % 2 == 0:
      return False
  return True

while isOdd(arr) == False:
  for i in range(0,length-1):
    if arr[i] % 2 == 0:
      if arr[i+1] %2 != 0:
       arr[i] , arr[i+1] = arr[i+1], arr[i]
       oddChange += 1

def isEven(arr):
  for i in range(0,evenCnt):
    if arr[i] % 2 != 0:
      return False
  return True

while isEven(arr2) == False:
  for i in range(0,length-1):
    if arr2[i] % 2 != 0:
      if arr2[i+1] %2 == 0:
       arr2[i] , arr2[i+1] = arr2[i+1], arr2[i]
       evenChange += 1
      
print(min(oddChange, evenChange))
