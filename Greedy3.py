S = input()
List = list(map(int, str(S)))

check = False
count = 0
target = List[0]

for i in range(len(List)):
  if List[i] == target:
    if check == False:
      continue
    if check == True:
      count += 1
      check = False
  if List[i] != target:
    check = True
    List[i] = target
    if i == len(List) - 1:
      count += 1
print(count)