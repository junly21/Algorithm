N = int(input())

answer = 2

for i in range(N):
    answer = answer + (answer -1)

print(answer**2)
