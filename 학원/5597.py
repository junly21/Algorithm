Class = []

for i in range(1, 31):
  Class.append(i)

for i in range(28):
  Class.remove(int(input()))

print(min(Class))
Class.remove(min(Class))
print(*Class)
