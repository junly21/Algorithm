N = str(input())
length = len(N)
half = length//2
left = 0
right = 0
 
for i in range(half):
    left += int(N[i])
for j in range(half,length):
    right += int(N[j])

if (left==right):
    print('LUCKY')
else:
    print('READY')
