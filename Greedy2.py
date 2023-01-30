Nums = input()  #숫자 받기
List = list(map(int, str(Nums)))  #숫자를 str로 쪼개서 int형변환 map한 뒤 list에 넣음

val = 0
index = 0

print(List)

for i in List:
  if index == 0 and i == 0:  #첫번째 수가 0
    index += 1
    continue
  elif index == 0 and i != 0:
    val += i
    index += 1
  elif index != 0 and i == 0:  #나오는 수가 0이면
    val += i
    index += 1
  elif index != 0 and i != 0:
    if val == 0:  #첫번째 수가 0 이었을 경우
      val += i
      index += 1
    else:
      val = val * i
      index += 1

  print(i)
  print(index)
  print(val)
  print("/n")

print(val)
