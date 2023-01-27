People = input()
Status = map(int, input().split())

List = list(Status)
List.sort()
print(List)

count = 0
group = 0

for i in List:
  count += 1
  if count >= i:
    group += 1
    count = 0

print(group)
