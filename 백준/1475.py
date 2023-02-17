N = input()
arr = [0] * 10
M = int(N)
for i in range(len(N)):
  n = int(N[i])
  if n == 6 or n == 9:
    if arr[6] == arr[9]:
      arr[9] += 1
    else:
      arr[6] += 1
  else:
    arr[n] += 1

print(max(arr))
